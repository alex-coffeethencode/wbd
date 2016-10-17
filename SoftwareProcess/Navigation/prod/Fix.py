'''
Created on Oct 10, 2016
Modified on Oct 16,2016

@author: Alex
'''

import math
from lib2to3.fixer_util import String
import Navigation.prod.Angle as Angle
import os.path
import xml.dom.minidom
import datetime
import time

class Fix():    
    logFile = ""
    sightFile = None    
    def __init__(self, fileIn = "output.txt"):
        logLine = "Start of log"
        
        if len(fileIn) < 1:
            raise ValueError("Fix.Fix:  Filename length GE 1")        
        try:
            stub = open(fileIn, "a+")
            stub.close()
        except:
             raise ValueError("Fix.Fix:  File not found")
        self.logFile = fileIn
        
        openedLog = open(self.logFile, "a+")
        openedLog.write(utcTimeStamp() + logLine + "\n")
        openedLog.clos
    def setSightingFile(self, sightingFile):
        if sightingFile == None:
            raise ValueError("Fix.setSightingFile:  File not passed")
        
        #check for valid extension and ensures .xml is not a valid name
        if sightingFile.find(".xml") > 0:
            try:
                stub = open(sightingFile, "a+")
                stub.close()
            except:
                raise ValueError("Fix.setSightingFile:  File not found")
            
            stub = self.sightFile
            self.sightFile = sightingFile
            
            # File Bool is true if file does not exist. In this case will return to original sightFile set in case multiple sight fiels can be set sequentially
            fileBool = self.checkIfFileExistsInLog()
            
            if fileBool == False:
                self.sightFile = stub
            return fileBool
        else:
            raise ValueError("Fix.setSightingFile:  File has invalid extension or not enough characters")
 
    def getSightings(self):
        obsveredAlt = 0.1
        
        if self.sightFile == None:
            raise ValueError("Fix.getSightings:  File not set")
    
        openedFile = open(self.sightFile)
        myDom = xml.dom.minidom.parse(openedFile)
        openedFile.close()

        mySight = myDom.getElementsByTagName("sighting")
        myLogArray = getSightingList(mySight)
        openedLog = open(self.logFile, "a")
        
        
        # NOte if myLogArray really is a value error better to write to log file first before error occurs
        if type(myLogArray) == ValueError:
            openedLog.write(utcTimeStamp() + "End of sighting file: " + self.sightFile + "\n")
            openedLog.close()
            raise myLogArray
          
        elif myLogArray == False:
            raise ValueError("Fix.setSightingFile:  myLogArray is returning False")
          
        else:
            for log in myLogArray:
                openedLog.write(utcTimeStamp() + log + "\n")
        
        openedLog.write(utcTimeStamp() +"End of sighting file: " + self.sightFile + "\n")
                        
        latitude = "0d0.0"
        longitude = "0d0.0"
        return (latitude, longitude)

    # func name + writes file to log if no already there
    def checkIfFileExistsInLog(self):
        openedLog = open(self.logFile, "r+")
        startLine = "Start of sighting file: " + self.sightFile
        
        for line in openedLog:
            if startLine in line:
                return False
            
        openedLog.close()
        # Line not found,append to log
        openedLog = open(self.logFile, "a+")
        openedLog.write(utcTimeStamp() + startLine + "\n")
        openedLog.close()
        return True

#?
# NEED TO CLARIFY FULL CITATION
#FROM:
#https://docs.python.org/2/library/xml.dom.minidom.html#dom-objects
def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

# My Additional  Methods:
#Calc returns rather than raises ValueError so that file can be appeneded 
def calcAdjAlt(optAct, obsAlt):
    myAngle = Angle.Angle()
    myAngle.setDegreesAndMinutes(obsAlt)
   
    if myAngle.getDegrees() < 0.1:
        return ValueError("Fix.setSightingFile:  Must be greater than 0.1")

    dip = 0
    refraction = 0
    try:
        if optAct[3] == "Natural":
            dip = (-0.97 * math.sqrt(float(optAct[0])))/60 
    except:
        return ValueError("Fix.setSightingFile:  Problems in calc dip ")
    
    try:    
        refraction = (-0.00452 * float(optAct[2])) / (273 + float(optAct[1])) / math.tan(myAngle.getDegrees())
    except:
        return ValueError("Fix.setSightingFile:  Problems in calc  refraction")
    
    try:
        otherAngle = Angle.Angle()
        otherAngle.setDegrees(dip + refraction)
        myAngle.add(otherAngle)
        return myAngle
    
    except:
        return ValueError("Fix.setSightingFile:  Problems adding angles")

def createLogEntry(reqAct, optAct):
    log = reqAct[0] + "\t" + reqAct[1] + "\t" +  reqAct[2] + "\t"
    adjAlt = Angle.Angle()
    
    adjAlt = calcAdjAlt(optAct, reqAct[3])
    
    if type(adjAlt) == ValueError:
        return adjAlt
    
    log = log + adjAlt.getString()
    return log

def getSightingList(mySight):
    # Sort by date then time then body    
    # Assumes sighting is mandatory
    if len(mySight) <= 0:
        return ValueError("Fix.getSightings:  no sightings found")
            
    sightingList = []

    requiredVar = ["body", "date", "time", "observation"]
    optionalVar = ["height", "temperature", "pressure", "horizon"]
    
    size = len(mySight)
    
    for ctr in range (size):
        print(str(ctr) + "\n")
        #Uninitialixed required elements
        reqAct = ["---","---","---","---"]
        # setDefualts
        optAct = [0,72,1010,"Natural"]
        
        #Must search by tag name. This process is more roundabout, but implemented befre disvocery of xml tree 
        #reqVar == tag name
        for reqVar in requiredVar:
            var = mySight[ctr].getElementsByTagName(reqVar)
            if len(var) > 0:
                reqAct[requiredVar.index(reqVar)] = getText(var[0].childNodes).strip()
            else:
                return ValueError("Fix.getSightings:  Required element not in sighting")
                
        for optVar in optionalVar:
            var = mySight[ctr].getElementsByTagName(optVar) 
            if len(var) > 0:
                optAct[optionalVar.index(optVar)] = getText(var[0].childNodes).strip()

        # Check req val filled in
        for required in reqAct:
            if required == "---":
                return ValueError("Fix.getSightings:  Missing required variable")
        
        # Just for assurance, assume capitilization is required in value:
        if optAct[3] != "Natural": 
            if optAct[3] != "Artificial" :
                return ValueError("Fix.setSightingFile:  Horizen must be either Natural or Artificial")
    
        entry = createLogEntry(reqAct, optAct) 

        # Extension of above prnciple, value erros returned rather than raised
        if type(entry) == ValueError:
            return entry

        sightingList.append(entry)
    return sightingList    

def utcTimeStamp():
    a = datetime.datetime.now()
    return ("LOG:\t"  + str(a) + ":\t")