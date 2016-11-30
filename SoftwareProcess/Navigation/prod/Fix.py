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

import xml.etree.ElementTree as ET

import datetime
import time
from cgi import logfile
from _elementtree import ParseError, XMLParser
from argparse import FileType

class Fix():    
    logFile = ""
    sightFile = None    
    ariesFile = None
    starFile = None
    errorNum = 0
    
    def __init__(self, logFile = "log.txt"):
        logLine = "Log file:"
        
        oldVal = self.logFile
        
        self.logFile = logFile
        
        if self.checkIfValueIsInLog(logFile):
            self.logFile = oldVal
        else:
            fileIn = logFile
            
            # Default
            if fileIn == "log.txt":
                self.logFile = fileIn
                self.errorNum = 0
                openedLog = open(self.logFile, "a+")
                openedLog.write(utcTimeStamp() + logLine + os.getcwd() + os.sep + logFile  +"\n")
                openedLog.close()   
            
            #if type(fileIn) == type(String):
            try:
                if len(fileIn) < 1:
                    raise ValueError("Fix.__init__:  Filename length GE 1")        
    
                stub = open(fileIn, "a+")
                self.errorNum = 0
                stub.write((utcTimeStamp() + logLine + os.getcwd() + os.sep + logFile  +"\n"))
                stub.close()
                
            except:
                raise ValueError("Fix.__init__:  ValueError on input " )#+ str(angle.degrees) + " " + str(angle.minutes))        
    
    
    def validateFile(self, fileName, fileExt, messageToLog, fileType):
        if fileName == None:
            return "  File not passed"
        
        #check for valid extension and ensures .xml is not a valid name
        if fileName.find(fileExt) > 0:
            try:
                stub = open(fileName, "r")
                stub.close()
                
                stub = open(self.logFile, "a+")
                stub.write(utcTimeStamp() + messageToLog + os.getcwd() + os.sep + fileName  +"\n")
                stub.close()
            except:
                return "  File not found"
            
            if fileType == "Sighting":
                stub = self.sightFile
                self.sightFile = fileName
                fileBool = self.checkIfFileExistsInLog()
            
                if fileBool == False:
                    self.sightFile = stub
                return True

            elif fileType == "Aries":
                stub = self.ariesFile
                self.ariesFile = fileName
                return True

            elif fileType == "Star":
                stub = self.starFile
                self.starFile = fileName
                return True
        else:
            return "  Error Found return Bad Extension"

    def setAriesFile(self, ariesFile=None):
        msg = "Aries file: "
        ext = ".txt"
        try:
            validFile = self.validateFile(ariesFile, ext, msg, "Aries")
        
            if validFile == True:
                return self.ariesFile
            else:
               raise ValueError("Fix.setAriesFile:  " + validFile)
        except:   
            raise ValueError("Fix.setAriesFile:  Error FOund")
    
    def setStarFile(self, starFile=None):
        msg = "Star file: "
        ext = ".txt"
        try:
            validFile = self.validateFile(starFile, ext, msg, "Star")
        
            if validFile == True:
                return self.starFile
            else:
               raise ValueError("Fix.setStarFile:  " + validFile)
        except:   
            raise ValueError("Fix.setStarFile:  Error FOund")
            
    def setSightingFile(self, sightingFile=None):
        msg = "Sighting file: "
        ext = ".xml"
        try:
            validFile = self.validateFile(sightingFile, ext, msg, "Sighting")
        
            if validFile == True:
                return self.sightFile
            else:
               raise ValueError("Fix.setSightingFile:  " + validFile)
        except:   
            raise ValueError("Fix.setSightingFile:  Error FOund")
    
    def getSightings(self):
        obsveredAlt = 0.1        
        errorNum = 0
        
        if self.sightFile == None:
            raise ValueError("Fix.getSightings:  File not set")
    
        if self.ariesFile == None:
            raise ValueError("Fix.getSightings:  Aries File not set")
    
        if self.starFile == None:
            raise ValueError("Fix.getSightings:  Star File not set")
    
        self.validateFileContents("Aries")
        self.validateFileContents("Star")
    
        openedFile = open(self.sightFile)
        myDom = xml.dom.minidom.parse(openedFile)
        openedFile.close()    
    
        mySight = myDom.getElementsByTagName("sighting")
        myLogArray = self.getSightingList(mySight)
        openedLog = open(self.logFile, "a+")
        
        # NOte if myLogArray really is a value error better to write to log file first before error occurs
        if type(myLogArray) == ValueError:
            raise myLogArray 

        elif myLogArray == False:
            pass
            #raise ValueError("Fix.setSightingFile:  myLogArray is returning False")  
        else:
            self.errorNum = self.errorNum + myLogArray[1]
            for log in myLogArray[0]:
                openedLog.write(utcTimeStamp() + log + "\n")
        
        openedLog.write(utcTimeStamp() +"Sighting errors:  " + self.getErrorNum() + "\n")
        openedLog.write(utcTimeStamp() +"End of sighting file: " + self.sightFile + "\n")
        openedLog.close()
    
        latitude = "0d0.0"
        longitude = "0d0.0"
        return (latitude, longitude)
    
    def getErrorNum(self):
        return str(self.errorNum)

    def checkIfValueIsInLog(self, queryStr):
        try:
            openedLog = open(self.logFile, "r+")
        except:
            return False
        for line in openedLog:
            if queryStr in line:
                return True
            
        openedLog.close()
        return False

    # func name + writes file to log if no already there
 
    def checkIfFileExistsInLog(self):
        openedLog = open(self.logFile, "r+")
        startLine = "Sighting file: " + self.sightFile
        
        for line in openedLog:
            if startLine in line:
                return False
            
        openedLog.close()
        return True

    # validates a file
    #return type error for bad input, 
        #else number of errors
    def validateFileContents(self, fileType):
        errorCount = 0
        
        if fileType == "Aries":
            file = open(self.ariesFile, "r")
            lines = file.readlines()
            
            for line in lines:
                try:
                    date, hour, alt = line.split("\t")
                    
                    #validate date
                    m,d,y = date.split("/")
                    if int(m) <= 12:
                        if int(m) < 10:
                            if int(m) > 0:
                                if  m[0] != '0':
                                    errorCount = errorCount + 1
                                else:
                                    pass # == 0
                            elif int(m) < 0:
                                errorCount = errorCount + 1
                        else:
                            pass # = 10,11, or 12
                    else:
                        errorCount = errorCount + 1
                    
                    #validate hour
                    hourInt = int(hour)
                    if hourInt >=0:
                        if(hourInt > 23):
                            errorCount = errorCount + 1
                        else:
                            pass
                    else:
                        errorCount = errorCount + 1
                        
                    #validate angle
                    try:
                        alt = alt.replace("\n","")
                        
                        myAngle = Angle.Angle()
                        myAngle.setDegreesAndMinutes(alt)
                        
                    except:
                        errorCount = errorCount + 1
             
                except:
                    # error in tabs/ spacing
                    errorCount = errorCount + 1
            file.close()
 
            self.errorNum = self.errorNum + errorCount
            return errorCount
        
        elif fileType == "Star":
            file = open(self.starFile, "r")
            lines = file.readlines()
            
            for line in lines:
                try:
                    body, date, lat, long = line.split("\t")
        
                    if len(body) > 0:
                        pass
                    else:
                        errorCount = errorCount + 1
                               
                    #validate date
                    m,d,y = date.split("/")
                    if int(m) <= 12:
                        if int(m) < 10:
                            if int(m) > 0:
                                if  m[0] != '0':
                                    errorCount = errorCount + 1
                                else:
                                    pass # == 0
                            elif int(m) < 0:
                                errorCount = errorCount + 1
                        else:
                            pass # = 10,11, or 12
                    else:
                        errorCount = errorCount + 1
                    
                except:
                    errorCount = errorCount + 1
         
         
                #validate angle - latitdue
                try:           
                    myAngle = Angle.Angle()
                    myAngle.setDegreesAndMinutes(lat)
                    
                except:
                    errorCount = errorCount + 1
         
                
                #validate angle - longoitude
                try:
                    long = long.replace("\n","")
                    
                    myAngle = Angle.Angle()
                    myAngle.setDegreesAndMinutes(long)
                    
                except:
                    errorCount = errorCount + 1
         
                    
            file.close()
            self.errorNum = self.errorNum + errorCount
            return errorCount
        
        elif fileType == "Sighting":
            return 0
        return -1
###################################################################################################################################################
    #?
    # NEED TO CLARIFY FULL CITATION
    #FROM:
    #https://docs.python.org/2/library/xml.dom.minidom.html#dom-objects
    def getText(self, nodelist):
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc)
    
    # My Additional  Methods:
    #Calc returns rather than raises ValueError so that file can be appeneded 
    def calcAdjAlt(self, optAct, obsAlt):
        myAngle = Angle.Angle()
        myAngle.setDegreesAndMinutes(obsAlt)
       
        if myAngle.getDegrees() < 0.1:
            return ValueError("Fix.setSightingFile:  Must be greater than 0.1")
       
        dip = 0
        refraction = 0
       
        try:
            if optAct[3].lower() == "natural":
                dip = -0.97/ 60
                dip = dip * math.sqrt(float(optAct[0]))
                
        except:
            return ValueError("Fix.setSightingFile:  Problems in calc dip ")
       
        try:    
    #        refraction = ( -0.00452 * pressure ) / ( 273 + celsius( temperature ) ) / tangent( altitude )                    
            a = (-0.00452 * float(optAct[2]))
            b = (273 + ((float(optAct[1]) - 32) / 1.8))
            c = math.tan(math.radians(myAngle.getDegrees()))
            
            refraction = a / b / c
        except:
            return ValueError("Fix.setSightingFile:  Problems in calc  refraction")
        try:        
            otherAngle = Angle.Angle()
            otherAngle.setDegrees(dip + refraction)
            
            myAngle.add(otherAngle)
            return myAngle
        
        except:
            return ValueError("Fix.setSightingFile:  Problems adding angles")
    
    def convertDateFormat(self, dateIn, minusDay):
        try:
            y,m,d = dateIn.split("-")
        except:
            return False
            #  print ("ERROR FOUND ****************    " + dateIn)
        
        if minusDay:
            m = str(int(m) - 1)
        date = m + "/"+ d + "/"+ y[2:]
        
        return date
    
    ## Doenst work!!!!
    def checkStarTable(self, star, date):
        if star == "Aries":
            file = open(self.ariesFile)
            allLines = file.readlines()
            file.close()
            
            for line in allLines:
                #print date
                check = self.convertDateFormat(date, False)
                if check == False:
                    date = self.convertDateFormat(date, True)
                else:
                    date = False#check
                #print date
                
                if date == False:
                    pass
                else:
                    pos = line.find(date)
                    if pos >= 0:
                        print date
                        return 21
        return 10
    
    def calcGeoPos(self, date):
        lat = "27d59.1"
        longt = "84d33.4"
        
        gha = self.checkStarTable("Aries", date)
    
        return "\t" + str(lat) + "\t" + str(longt)
    
    def createLogEntry(self, reqAct, optAct):
        log = reqAct[0] + "\t" + reqAct[1] + "\t" +  reqAct[2] + "\t"
        adjAlt = Angle.Angle()
        
        adjAlt = self.calcAdjAlt(optAct, reqAct[3])
        
        if type(adjAlt) == ValueError:
            return adjAlt
    
        log = log + adjAlt.getString()
        
        geoPos = self.calcGeoPos(reqAct[1])
        
        if type(adjAlt) == ValueError:
            return adjAlt
    
        log = log + "\t" + geoPos
    
        return log
    
    def getSightingList(self,mySight):
        # Sort by date then time then body    
        # Assumes sighting is mandatory
        if len(mySight) <= 0:
            return False;
        #        return ValueError("Fix.getSightings:  no sightings found")
        
        errorNum = 0
        errorFound = False
        sightingList = []
    
        requiredVar = ["body", "date", "time", "observation"]
        optionalVar = ["height", "temperature", "pressure", "horizon"]
        
        size = len(mySight)
            
        for ctr in range (size):
            errorFound = False
            #Uninitialixed required elements
            reqAct = ["---","---","---","---"]
            # setDefualts
            optAct = [0,72,1010,"Natural"]
            
            #Must search by tag name. This process is more roundabout, but implemented befre disvocery of xml tree 
            #reqVar == tag name
            for reqVar in requiredVar:
                var = mySight[ctr].getElementsByTagName(reqVar)
                if len(var) > 0:
                    reqAct[requiredVar.index(reqVar)] = self.getText(var[0].childNodes).strip()
                else:
                    errorFound = True                #return ValueError("Fix.getSightings:  Required element not in sighting")
            if errorFound:
                errorNum = errorNum + 1
                break        
            
            for optVar in optionalVar:
                var = mySight[ctr].getElementsByTagName(optVar) 
                if len(var) > 0:
                    optAct[optionalVar.index(optVar)] = self.getText(var[0].childNodes).strip()
    
            # Check req val filled in
            for required in reqAct:
                if required == "---":
                    errorFound = True
                    #return ValueError("Fix.getSightings:  Missing required variable")
                if required == "":
                    errorFound = True
                    #return ValueError("Fix.getSightings:  Missing required variable")
            if errorFound:
                errorNum = errorNum + 1
                break        
            
            # Just for assurance, assume capitilization is required in value:
            if optAct[3].lower() != "natural": 
                if optAct[3].lower() != "artificial" :
                    errorFound = True
                    #return ValueError("Fix.setSightingFile:  Horizen must be either Natural or Artificial")
            if errorFound:
                errorNum = errorNum + 1
                break        
            
            entry = self.createLogEntry(reqAct, optAct) 
    
            # Extension of above prnciple, value erros returned rather than raised
            if type(entry) == ValueError:
                errorNum = errorNum + 1    
                #return entry
            else:
                sightingList.append(entry)
                
        return (sightingList, errorNum)

def utcTimeStamp():
    a = datetime.datetime.now()
    return ("LOG:\t"  + str(a) + ":\t")
