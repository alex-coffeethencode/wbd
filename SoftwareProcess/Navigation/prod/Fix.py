'''
Created on Oct 10, 2016
Modified on Dec 3,2016

@author: Alex
'''

import math
from lib2to3.fixer_util import String
import Navigation.prod.Angle as Angle

import Navigation.prod.Entry as Entry
import os.path
import xml.dom.minidom

import datetime

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
                return False
            
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
            return False
    def setAriesFile(self, ariesFile=None):
        msg = "Aries file: "
        ext = ".txt"
        try:
            validFile = self.validateFile(ariesFile, ext, msg, "Aries")
            if validFile == False:
                raise ValueError("Fix.setAriesFile:  Error FOund")
            return self.ariesFile
        except:   
            raise ValueError("Fix.setAriesFile:  Error FOund")
    
    def setStarFile(self, starFile=None):
        msg = "Star file: "
        ext = ".txt"
        try:
            validFile = self.validateFile(starFile, ext, msg, "Star")
            if validFile == False:
                raise ValueError("Fix.setStarFile:  Error FOund")
            return self.starFile
        except:   
            raise ValueError("Fix.setStarFile:  Error FOund")
            
    def setSightingFile(self, sightingFile=None):
        msg = "Sighting file: "
        ext = ".xml"
        try:
            validFile = self.validateFile(sightingFile, ext, msg, "Sighting")
            if validFile == False:
                raise ValueError("Fix.setSightingFile:  Error FOund")

            return self.sightFile
        except:   
            raise ValueError("Fix.setSightingFile:  Error FOund")
    
    def getSightings(self, assumedLat = "0d0.0", assumedLong = "0d0.0"):
        if self.checkGetSightingParam(assumedLat, assumedLong):
            #? write to log?
            raise ValueError("Fix.getSightings:  Bad Parameter")
        if not self.checkGetSightingFileSet():
#           #? write to log?
          raise ValueError("Fix.getSightings:  File not Set")
        
        #entryLog = createEntryLog()
        errorNum = 0
        entryLog = self.createEntryLog()
        #errorNum = errorNum + self.validateFileContents("Aries")
        #errorNum = errorNum + self.validateFileContents("Star")
            
        self.writeToLog(entryLog, assumedLat, assumedLong)
   
    def searchFile(self,fileIn, term):
        openedLog = open(fileIn, "r+")
        
        for line in openedLog:
            if term in line:
                openedLog.close()
                return line
            
        openedLog.close()
        return "Not Found"
    
   
        
    def writeToLog(self, entryLog, assLat, assLong):
        assLatOrig = assLat
        assLongOrig = assLong
        
        totalLat = '--'
        totalLong = '--'
        
        
        # Skip sorting for now        
        totalErrors = entryLog[1]
        listOfEntries = entryLog[0]
        if len(listOfEntries):
            # final validation
            for value in listOfEntries:
                result =  self.checkStarTable(value.body, value.changeDateFormat(value.date))
                
                bod, boda,dat,lta,lng = "a","a","a","a","a"
                dateA,dateB = "b","b"
                hrA,hrB = "",""
                angA,angB = "",""
                    
                if result == "NOT FOUND":
                    listOfEntries.remove(value)
                else:    
                    # Star Data:
                    try:
                        bod,dat,lng,lat = result.split()
                    except:
                        bod,boda, dat,lng,lat = result.split()
                
                result =  self.checkStarTable("Aries", [value.changeDateFormat(value.date), value.time])
                if result == "NOT FOUND":
                    listOfEntries.remove(value)
                else:    
                    dateA = result[0]
                    dataA, hrA, angA = dateA.split()
                    dateB = result[1]
                    dataB, hrB, angB = dateB.split()
                
               #  // Validation
                testerAngle = Angle.Angle()
                try:
                    testerAngle.setDegreesAndMinutes(lng)
                    testerAngle.setDegreesAndMinutes(lat)
                except:
                    totalErrors = totalErrors + 1
                    break
                        
                assLatAng = Angle.Angle()
                assLongAng = Angle.Angle()
                
                mult = 1
                
                
                if assLat[0] == 'S':
                    mult = -1
                    assLat = assLat[1:] 
                    assLatAng.setDegreesAndMinutes(assLat)
                    assLatAng.degrees = assLatAng.degrees + 180
                    
                if assLat[0] == 'N':
                    assLat = assLat[1:] 
                    assLatAng.setDegreesAndMinutes(assLat)          
                
                if lat[0] == 'S':
                    lat = lat[1:] 
                    
                if lat[0] == 'N':
                    lat = lat[1:] 
                
                assLongAng.setDegreesAndMinutes(assLong)
        
                angleA = Angle.Angle()   
                angleB = Angle.Angle()
                
                geoLong = Angle.Angle()
                geoLat = Angle.Angle()
                angleInitLng = Angle.Angle()
                
                angleA.setDegreesAndMinutes(angA)   
                angleB.setDegreesAndMinutes(angB)   
                geoLong.setDegreesAndMinutes(lng)

                geoLat.setDegreesAndMinutes(lat)
                print "geo    " + geoLat.getString()
                    
                geoLong = value.calcGeo(angleA,angleB, geoLong)    
                
                geoLongString = geoLong.getString()
                geoLatString = geoLat.getString()
                
                angleInitLng.setDegreesAndMinutes(assLong)
                ap = value.adjPos(geoLong,angleInitLng, assLatAng, geoLat, mult)
                        
                azimuth = ap[1].getString()
                ap = ap[0]
                
                #distance adjusted
                da = ap
                ## adjusted altitude
                aa = value.calcAdjAlt()
                
                if type(aa) == ValueError:
                    totalErrors = totalErrors + 1
                    break

                
                bb = Angle.Angle()
                bb.setDegreesAndMinutes(aa.getString())
                da.subtract(bb)

                min,sec = da.getString().split('d')
                if sec[0] == '0':
                    sec = sec[1:]
                
                daArcMin = round(int(min) * 60 + float(sec))

            # Sorting
            #listOfEntries.sort()
            
            openedLog = open(self.logFile, "a+")
            outputString = " "   
            try:   
                  # write to log
                for value in listOfEntries: 
                    outputString = outputString + utcTimeStamp() 
                    outputString = outputString + value.body 
                    outputString = outputString + "\t" + value.observation 
                    outputString = outputString + "\t" + value.time
                    outputString = outputString + "\t" + aa.getString()
                    outputString = outputString + "\t" + geoLatString 
                    outputString = outputString + "\t" + geoLongString  #value.calcGe
                    outputString = outputString + "\t" + assLatOrig
                    outputString = outputString + "\t" + assLongOrig
                    outputString = outputString + "\t" + azimuth
                    outputString = outputString + "\t" + str(daArcMin) +  " \n"
                    
                    openedLog.write(outputString)
            except:
                totalErrors = totalErrors + 1    
        ###### SUM UP LAT & LONG
        
        
        ####
        outputString = utcTimeStamp() +  "Sighting errors: " + str(totalErrors)
        openedLog.write(outputString)    
        outputString =  utcTimeStamp() + "Approximate Latitude: " + assLatOrig + "  Approximate Longitude: " + assLongOrig
        openedLog.write(outputString)
        openedLog.close()

        return (totalLat, totalLong)

    def createEntryLog(self):
        openedFile = open(self.sightFile)
        myDom = xml.dom.minidom.parse(openedFile)
        openedFile.close()    
    
        mySight = myDom.getElementsByTagName("sighting")
        myLogArray = self.getSightingList(mySight)
        
        return myLogArray
        
        
    def checkGetSightingFileSet(self):
        if self.sightFile == None:
            return False
        else:
            try:
                openTest = open(self.sightFile, "r+")
                openTest.close()
            except:
                return False
        if self.ariesFile == None:
            return False
        else:
            try:
                openTest = open(self.ariesFile, "r+")
                openTest.close()
            except:
                return False
        if self.starFile == None:
            return False
        else:
            try:
                openTest = open(self.starFile, "r+")
                openTest.close()
            except:
                return False
        return True
    
    # TEchically doesnt have to be self
    def checkGetSightingParam(self, assLat, assLong):
        if isinstance(assLat, basestring) == False:
            return True
        if isinstance(assLong, basestring) == False:
            return True
        
        firstChar = assLat[0];
        
        if firstChar == 'N' or  firstChar == 'S':
            if assLat[1:] == "0d0.0":
                return True
        else:
            # If latituade is really on equator, check legal longitude
            if assLat != "0d0.0":
                return True          
            else:
                try:
                    myAngle = Angle.Angle()
                    myAngle.setDegreesAndMinutes(assLong)
                except:
                    return True
                return False
        try:
            myAngle = Angle.Angle()
            myAngle.setDegreesAndMinutes(assLat[1:])    
            myAngle.setDegreesAndMinutes(assLong)
        except:
            return True
        
        return False
    
    
    
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
        if fileType == "Star":
            
            return True
        elif fileType == "Aries":
            return True
        elif fileType == "Sighting":
            return True
        return -1
       
    ##################################################################################################################################################
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
    
#11
    def checkStarTable(self, star, date):
        if star == "Aries":
            file = open(self.ariesFile)
            allLines = file.readlines()
            file.close()
            calender = date[0]
            hour = date[1][0:2]

            bestLine = "NOT FOUND"
            allLines = iter(allLines)
            for line in allLines:
                if calender in line:
                    
                    if hour in line[8:11]:    
                        nextHr = next(allLines)
                        return (line, nextHr)
                        break
            
            pass
        else:
            file = open(self.starFile)
            allLines = file.readlines()
            file.close()
            
            bestLine = "NOT FOUND"
            for line in allLines:
                if star in line:
                    if date in line:
                        return line
                    else:
                        try:
                            bod,dat,lta,lng = line.split()
                            m1=int(date[:2])
                            m2=int(dat[:2])
                            
                            d1 = int(date[3:-3])
                            d2 = int(dat[3:-3])
                            
                            if m1 - m2 >= 0 and d1 - d2 >= 0:
                                bestLine = line

                        except:
                            # Some stars have spaces in their names
                            try:                                    
                                boda, bodb,dat,lta,lng = line.split()
                                
                                m1=int(date[:2])
                                m2=int(dat[:2])
                                
                                d1 = int(date[3:-3])
                                d2 = int(dat[3:-3])
                                
                                if m1 - m2 >= 0 and d1 - d2 >= 0:
                                    bestLine = line
                            except:
                                continue          
            return bestLine
        return "NOT FOUND"
    
    
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
            myEntry = Entry.Entry()    
            
            if not myEntry.createEntry(mySight[ctr]):
                errorNum = errorNum + 1
            else:
                sightingList.append(myEntry)
    
        return (sightingList, errorNum)

def utcTimeStamp():
    a = datetime.datetime.now()
    return ("LOG:\t"  + str(a) + ":\t")
