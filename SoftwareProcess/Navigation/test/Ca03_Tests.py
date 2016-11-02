
import unittest
#import Navigation.prod.Fix as Fix
import Navigation.prod.Fix as Fix
import math

import os.path

#20 min of test code writing with ~= 2 hours prep

#coding 1154 10/10

class Ca03_Test(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

#Individual Box Testing:

#m1 =  Fix() (The constructor)
    #Assert Valid contructor
    def test100_010_ShouldConstruct(self):
        self.assertIsInstance(Fix.Fix(), Fix.Fix)

    # //2 = file input functions
    # 200 = setSightingFile
    
    def test200_001FilenameGTEOne(self):
        expectedString = "Fix.setSightingFile:"
        myFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:   
            myFix.setSightingFile(".xml")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    
    def test200_002A(self):
        expectedString = "Fix.setSightingFile:"
        myFix = Fix.Fix()
        with self.assertRaises(ValueError) as context:   
            myFix.setSightingFile(".xml")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])



    def test300_010checkFilesAreSet(self):
        if(os.path.isfile("output.txt")):
            os.remove("output.txt")
            
        myFix = Fix.Fix("output.txt")
        
    
        myFix.setSightingFile("f.xml")
        myFix.setAriesFile("aries.txt")
        myFix.setStarFile("stars.txt")
        
        self.assertEquals("f.xml",myFix.sightFile)
        self.assertEquals("aries.txt",myFix.ariesFile)
        self.assertEquals("stars.txt",myFix.starFile)



    def test500_010(self):
        pass
        
    #should check for abs path
#    def test500_020checkLogForFiles(self):
#        ariesString = "Sighting file:/t"
 #       ariesString = "Aries file:/t"
  #      starString = "Star file:/t"
        
    def test600_010validateAriesContents(self):    
        if(os.path.isfile("output.txt")):
            os.remove("output.txt")
        myFix = Fix.Fix("output.txt")
        myFix.setAriesFile("aries.txt")
        
        self.assertEquals(0,myFix.validateFileContents("Aries"))
    def test600_020validateStarContents(self):    
        if(os.path.isfile("output.txt")):
            os.remove("output.txt")
        myFix = Fix.Fix("output.txt")
        myFix.setStarFile("stars.txt")
        
        self.assertEquals(0,myFix.validateFileContents("Star"))

    def test600_030calcGeoPos(self):
        if(os.path.isfile("output.txt")):
            os.remove("output.txt")
        myFix = Fix.Fix("output.txt")
        myFix.setSightingFile("f.xml")
        myFix.setStarFile("stars.txt")
        myFix.setAriesFile("aries.txt")
        
        myFix.getSightings()
        
        self.assertEquals(1,1)


    # test for cao3 example
    def test700_010testLogFileForValidGeoPos(self):
        logFile = "output.txt"
        if(os.path.isfile(logFile)):
            os.remove(logFile)
        myFix = Fix.Fix(logFile)
        myFix.setSightingFile("sightingFile.xml")
        myFix.setStarFile("stars.txt")
        myFix.setAriesFile("aries.txt")        
        myFix.getSightings()
        
#        targetStringList = ["Hadar", "2016-03-01", "23:40:01", "29d55.7"]
#LOG: 2016-10-01 10:01:10-06:00 Pollux      2017-04-14     23:50:14     15d01.5     27d59.1     84d33.4

        targetStringList = ["Pollux", "2017-04-14", "23:50:14", "15d01.5", "27d59.1","84d33.4"]
        
        theLogFile = open(logFile, "r")
        logFileContents = theLogFile.readlines()
        theLogFile.close()
       
        sightingCount = 0
        for logEntryNumber in range(0, len(logFileContents)):
            print (logFileContents[logEntryNumber])
            if(logFileContents[logEntryNumber].find(targetStringList[0]) > -1):
                sightingCount += 1
                for target in targetStringList:
                    self.assertNotEquals(-1, logFileContents[logEntryNumber].find(target), 
                                         "Major:  Log entry is not correct for getSightings")
        self.assertEquals(1, sightingCount) 
        
        
'''
    def test300_080_ShouldLogStarWithNaturalHorizon(self):
        testFile = "CA02_300_ValidOneStarNaturalHorizon.xml"
        targetStringList = ["Hadar", "2016-03-01", "23:40:01", "29d55.7"]
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix.setSightingFile(testFile)
        theFix.getSightings()
        
        theLogFile = open(self.RANDOM_LOG_FILE, "r")
        logFileContents = theLogFile.readlines()
        theLogFile.close()
        
        sightingCount = 0
        for logEntryNumber in range(0, len(logFileContents)):
            if(logFileContents[logEntryNumber].find(targetStringList[0]) > -1):
                sightingCount += 1
                for target in targetStringList:
                    self.assertNotEquals(-1, logFileContents[logEntryNumber].find(target), 
                                         "Major:  Log entry is not correct for getSightings")
        self.assertEquals(1, sightingCount)
        self.cleanup()  
'''