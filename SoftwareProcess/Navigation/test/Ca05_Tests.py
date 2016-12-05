import unittest
import Navigation.prod.Fix as Fix
import Navigation.prod.Angle as Angle
import Navigation.prod.Entry as Entry

import math
import os.path

class Ca05_Test(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

#Individual Box Testing:

#TEst cdes:

#Accpetance
#500: getSighting as an accpetance test

#"Unit Tests" through acceptance test methods
#<100 = Old results tests, taken from Cabvas comments
#600 : getSightingParam
#700 : checkGetSightingsFileSet
#800 : createEntryLog
#    810 = sightingFile problem
#    820 - star file pblm
#    830 = aries file pblm
#    850 = adj clalc unit tests
#900 : writeToLog

    
    def test500_010_CheckFirstEntryOfSample(self):     
        '''
        if(os.path.isfile("log.txt")):
            os.remove("log.txt")           
        
        theFix = Fix.Fix()                            
        sightingFilePath = "sightingFile_CA05.xml"
        #sightingFilePath="f.xml"
        
        theFix.setSightingFile(sightingFilePath)                            
        starFilePath = theFix.setStarFile("stars.txt")                            
        ariesFilePath = theFix.setAriesFile("aries.txt")                            
    
        assumedLatitude = "N27d59.5"                            
        assumedLongitude = "85d33.4"                            
        approximatePosition = theFix.getSightings(assumedLatitude, assumedLongitude)                            

    '''
                            
        '''                    
        Concluding contents of "log.txt":                            
        LOG: 2016-10-01 10:01:09-06:00 Log file: /git/SoftwareProcess/SoftwareProcess/Navigation/test/log.txt                            
        LOG: 2016-10-01 10:01:10-06:00 Sighting file:  /git/SoftwareProcess/SoftwareProcess/Navigation/test/sightings.xml                            
        LOG: 2016-10-01 10:01:10-06:00 Aries file:  /git/SoftwareProcess/SoftwareProcess/Navigation/test/aries.txt                            
        LOG: 2016-10-01 10:01:10-06:00 Star file:  /git/SoftwareProcess/SoftwareProcess/Navigation/test/star.txt                            
        LOG: 2016-10-01 10:01:10-06:00 Pollux      2017-04-14     23:50:14     15d01.5     27d59.1     84d33.4    N27d59.5    85d33.4    292d44.6    174                            
        LOG: 2016-10-01 10:01:10-06:00 Sighting errors:      1                            
        LOG: 2016-10-01 10:01:11-06:00 Approximate latitude:      N29d6.8         Approximate longitude:    82d52.9                              
        '''
        pass 
    


    def test500_020_ExcelExampleRigil(self):
        if(os.path.isfile("log.txt")):
            os.remove("log.txt")                   
        theFix = Fix.Fix()                            
        sightingFilePath = "excelExample.xml"

        logFile = "output.txt"
        if(os.path.isfile(logFile)):
            os.remove(logFile)
        myFix = Fix.Fix(logFile)
        myFix.setSightingFile(sightingFilePath)
        myFix.setStarFile("stars.txt")
        myFix.setAriesFile("aries.txt")        
        
        assumedLatitude = "S53d38.4"                            
        assumedLongitude = "74d35.3" 
        myFix.getSightings(assumedLatitude, assumedLongitude)
        
        targetStringList = ["Rigil", "35d08.1", "-60d53.8", "318d09.9", "125d37.7", "2159"]    #, "2017-04-14", "23:50:14", "15d01.5", "27d59.1","84d33.4"]   
        
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
       
           
    def test700_010testLogFileForValidGeoPos(self):
        logFile = "output.txt"
        if(os.path.isfile(logFile)):
            os.remove(logFile)
        myFix = Fix.Fix(logFile)
        myFix.setSightingFile("sightingFile.xml")
        myFix.setStarFile("stars.txt")
        myFix.setAriesFile("aries.txt")        
        myFix.getSightings()
        
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
        #self.assertEquals(1, sightingCount) 
        
        
    def test600_010twoBadParam(self):
        if(os.path.isfile("output.txt")):
            os.remove("output.txt")           
        myFix = Fix.Fix("output.txt")
    
        expectedString = "Fix.getSightings:  "
        with self.assertRaises(ValueError) as context:
            myFix.getSightings(1,2);
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    
    

    def test600_020_FirstBadParam(self):
        if(os.path.isfile("output.txt")):
            os.remove("output.txt")           
        myFix = Fix.Fix("output.txt")
    
        expectedString = "Fix.getSightings:  "
        with self.assertRaises(ValueError) as context:
            myFix.getSightings("0d0.0", 0) 
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    
    def test600_021_FirstBadParam_NoValue(self):
        if(os.path.isfile("output.txt")):
            os.remove("output.txt")           
        myFix = Fix.Fix("output.txt")
    
        expectedString = "Fix.getSightings:  "
        with self.assertRaises(ValueError) as context:
            myFix.getSightings("", 0) 
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    
    
    def test600_030_SecondBadParam(self):
        if(os.path.isfile("output.txt")):
            os.remove("output.txt")           
        myFix = Fix.Fix("output.txt")
    
        expectedString = "Fix.getSightings:  "
        with self.assertRaises(ValueError) as context:
            myFix.getSightings(0, "0d0.0")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    

    def test600_040_BadCardinalDirectionForLat(self):
        if(os.path.isfile("output.txt")):
            os.remove("output.txt")           
        myFix = Fix.Fix("output.txt")
    
        expectedString = "Fix.getSightings:  "
        with self.assertRaises(ValueError) as context:
            myFix.getSightings("w0d0.0", "0d0.0")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    
    
    def test600_050_LatNotLegal(self):
        if(os.path.isfile("output.txt")):
            os.remove("output.txt")           
        myFix = Fix.Fix("output.txt")
    
        expectedString = "Fix.getSightings:  "
        with self.assertRaises(ValueError) as context:
            myFix.getSightings("North", "0d0.0")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    
        
    def test600_060_LegalEq_IllegalLong(self):
        if(os.path.isfile("output.txt")):
            os.remove("output.txt")           
        myFix = Fix.Fix("output.txt")
    
        expectedString = "Fix.getSightings:  "
        with self.assertRaises(ValueError) as context:
            myFix.getSightings("0d0.0", "0.0")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    

    def test600_070_IllegalEQ(self):
        if(os.path.isfile("output.txt")):
            os.remove("output.txt")           
        myFix = Fix.Fix("output.txt")
    
        expectedString = "Fix.getSightings:  "
        with self.assertRaises(ValueError) as context:
            myFix.getSightings("S0d0.0", "1d1.1")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])


     
    def test700_010_NoSighting(self):
        if(os.path.isfile("output.txt")):
            os.remove("output.txt")           
        myFix = Fix.Fix("output.txt")
        myFix.setSightingFile("f.xml")
        expectedString = "Fix.getSightings:  "
        
        
        myOPen = open("f.xml", "r+")
        myOPen.close()
        
        
        with self.assertRaises(ValueError) as context:
            myFix.getSightings("N1d0.0", "1d1.1")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
            
    def test700_020_NoStarFile(self):
        if(os.path.isfile("output.txt")):
            os.remove("output.txt")           
        myFix = Fix.Fix("output.txt")
        myFix.setSightingFile("f.xml")

        expectedString = "Fix.getSightings:  "
        with self.assertRaises(ValueError) as context:
            myFix.getSightings("N1d0.0", "1d1.1")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

    def test700_030_NoAriesFile(self):
        if(os.path.isfile("output.txt")):
            os.remove("output.txt")           
        myFix = Fix.Fix("output.txt")
        myFix.setSightingFile("f.xml")
        myFix.setStarFile("stars.txt")

        expectedString = "Fix.getSightings:  "
        with self.assertRaises(ValueError) as context:
            myFix.getSightings("N1d0.0", "1d1.1")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])


    ## unit tests supplied by cellNav
    def test850_010_calcAdj_Rigil(self):
        if(os.path.isfile("output.txt")):
            os.remove("output.txt")           

        myFix = Fix.Fix("output.txt")        

        reqAct = ["Rigil Kentaurus", "2017-03-24", "23:41:56", "35d14.8"]
        optAct = [31, 72, 1010, 'natural']
        
        exp = "35d08.1"
        obsAlt = reqAct[3]
        myEntry = Entry.Entry()
        
        
#        expectedString = "Fix.writeToLog:  "
#        with self.assertRaises(ValueError) as context:            
#                res = myEntry.calcAdjAlt()
                #res = res.getString()
                

        res = myEntry.calcAdjAlt()
               

        #self.assertEqual(res, exp)

### ----------------### ---------------### -------------##

    def test50_910_ShouldRaiseExceptionOnMissingPam(self):
        expectedString = "Angle.add:  "
        myAngle = Angle.Angle()
        with self.assertRaises(ValueError) as context:
            myAngle.add()
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])


    def test50_920_ShouldRaiseExceptionOnNonangleParm(self):
        expectedString = "Angle.add:  "
        myAngle = Angle.Angle()

        with self.assertRaises(ValueError) as context:
            myAngle.add(5)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])


    def test60_910_ShouldRaiseExceptionOnMissingPam(self):
        expectedString = "Angle.subtract:  "
        myAngle = Angle.Angle()
        
        with self.assertRaises(ValueError) as context:
            myAngle.subtract()
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])


    def test60_920_ShouldRaiseExceptionOnNonangleParm(self):
        expectedString = "Angle.subtract:  "
        myAngle = Angle.Angle()
        with self.assertRaises(ValueError) as context:
            myAngle.subtract(5)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

    def test70_910_ShouldRaiseExceptionOnMissingPam(self):
        expectedString = "Angle.compare:  "
        myAngle = Angle.Angle()
        
        with self.assertRaises(ValueError) as context:
            myAngle.compare()
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

            
    def test30_030_ShouldReturnDegreesWithRounding(self):
        anAngle = Angle.Angle()
        anAngle.setDegrees(10.5/60.0)
        
        self.assertAlmostEquals(10.5/60.0, anAngle.getDegrees(),places=4)


    def test300_040_ShouldReturnModuloDegreesWithRounding(self):
        anAngle = Angle.Angle()
        anAngle.setDegrees(10.5/60.0)
        
        self.assertAlmostEquals(10.5/60.0, anAngle.getDegrees(),places=4)

    def test400_050_ShouldSetAngleWithValidNegXY(self):
        anAngle = Angle.Angle()
        anAngle.setDegrees(340.175 - 360)
        data = (340.175 - 360)
        
        
        print data  
        
        self.assertAlmostEquals(anAngle.setDegrees(data), 340.175)

#AssertionError: 340.175 != 339.825 within 7 places


#AssertionError: 0.175 != 0.17433333333332257 within 4 places
#AssertionError: 0.175 != 0.17433333333333334 within 4 places











'''
    def test900_010_CheckWrtireLog(self):

        if(os.path.isfile("output.txt")):
            os.remove("output.txt")           
        myFix = Fix.Fix("output.txt")
        myFix.setSightingFile("f.xml")
        myFix.setStarFile("stars.txt")

        expectedString = "Fix.getSightings:  "
        
        myFix.getSightings("N1d0.0", "1d1.1")

 #       self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])


    def test900_020_ShouldLogStarWithNaturalHorizon(self):
        testFile = "CA02_300_ValidOneStarNaturalHorizon.xml"
        targetStringList = ["Hadar", "2016-03-01", "23:40:01", "29d55.7"]
        
        theFix = Fix.Fix(self.RANDOM_LOG_FILE)
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

    Rigil:
    
    Sighting File Information (relevant lines only)                
    date =    2017-03-24            
    time=    23:41:56    UTC        
    altitude =     35    degrees    14.8    minutes
    height=    31    ft        
    horizon =    natural            
    pressure=    1010    mbar        
    temp=    72    degrees F        
    Star Chart Information (relevant lines only)                
    Rigil Kentaurus    2017-03-22    139d48.6     -60d53.8    
    Aries Information (relevant lines only)                
    2017-03-24    23    167d50.6        
    2017-03-25    0    182d53.1        
    Assumed Position (provided via parameter)                
    lat =    S53d38.4            
    long =    74d35.3            
    
    '''












    
    
    
'''
    
        #old tests 
    
    
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


'''



======================================================================
FAIL: test300_050_ShouldReturnModuloNegativeDegreesWithRounding (Navigation.test.AngleTestTA.AngleTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\AngleTestTA.py", line 131, in test300_050_ShouldReturnModuloNegativeDegreesWithRounding
    self.assertAlmostEquals(359.826667, anAngle.getDegrees(),places=4)
AssertionError: 359.826667 != 359.826 within 4 places


======================================================================
FAIL: test400_930_ShouldRaiseExceptionOnMissingD (Navigation.test.AngleTestTA.AngleTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\AngleTestTA.py", line 242, in test400_930_ShouldRaiseExceptionOnMissingD
    self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)])
AssertionError: 'Angle.setDegreesAndMinutes:' != 'substring not found'

======================================================================
FAIL: test400_940_ShouldRaiseExceptionOn2DecimalY (Navigation.test.AngleTestTA.AngleTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\AngleTestTA.py", line 250, in test400_940_ShouldRaiseExceptionOn2DecimalY
    anAngle.setDegreesAndMinutes("10d5.55")
AssertionError: ValueError not raised

======================================================================
FAIL: test400_960_ShouldRaiseExceptionOnNonintegerY (Navigation.test.AngleTestTA.AngleTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\AngleTestTA.py", line 269, in test400_960_ShouldRaiseExceptionOnNonintegerY
    self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)])
AssertionError: 'Angle.setDegreesAndMinutes:' != 'could not convert string to'

======================================================================
FAIL: test400_970_ShouldRaiseExceptionOnMissingY (Navigation.test.AngleTestTA.AngleTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\AngleTestTA.py", line 278, in test400_970_ShouldRaiseExceptionOnMissingY
    self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)])
AssertionError: 'Angle.setDegreesAndMinutes:' != 'could not convert string to'

----------------------------------------------------------------------
Ran 50 tests in 0.033s

FAILED (failures=8, errors=4)
Cesar Sanchez , Dec 3 at 10:03pm
Fix:

Finding files... done.
Importing test modules ... done.

======================================================================
ERROR: test100_920_ShouldRaiseExceptionOnNonStringFile (Navigation.test.FixTestCA03.TestFix)
Construct Fix with invalid parm
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 171, in test100_920_ShouldRaiseExceptionOnNonStringFile
    F.Fix(42)
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\prod\Fix.py", line 22, in __init__
    if len(fileIn) < 1:
TypeError: object of type 'int' has no len()

======================================================================
ERROR: test200_010_ShouldSetSightingFileWithOutKeywordParm (Navigation.test.FixTestCA03.TestFix)
Set sighting file without keyword parm
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 211, in test200_010_ShouldSetSightingFileWithOutKeywordParm
    self.assertNotEquals(-1, result.find(testFile),
AttributeError: 'bool' object has no attribute 'find'

======================================================================
ERROR: test200_020_ShouldConstructWithKeywordParmCA03 (Navigation.test.FixTestCA03.TestFix)
Set sighting file with keyword parm
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 225, in test200_020_ShouldConstructWithKeywordParmCA03
    self.assertNotEquals(-1, result.find(testFile),
AttributeError: 'bool' object has no attribute 'find'

======================================================================
ERROR: test200_030_ShouldSetValidSightingFile (Navigation.test.FixTestCA03.TestFix)
Set sighting file and verify string is written to file
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 236, in test200_030_ShouldSetValidSightingFile
    with open(self.DEFAULT_LOG_FILE, "r") as theLogFile:
IOError: [Errno 2] No such file or directory: 'log.txt'

======================================================================
ERROR: test200_910_ShouldRaiseExceptionOnNonStringFileName (Navigation.test.FixTestCA03.TestFix)
Fail on setting sighting file with non-string name
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 250, in test200_910_ShouldRaiseExceptionOnNonStringFileName
    theFix.setSightingFile(testFile)
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\prod\Fix.py", line 39, in setSightingFile
    if sightingFile.find(".xml") > 0:
AttributeError: 'int' object has no attribute 'find'

======================================================================
ERROR: test200_950_ShouldRaiseExceptionOnMissingFileName (Navigation.test.FixTestCA03.TestFix)
Fail on setting star sighting file with no name
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 291, in test200_950_ShouldRaiseExceptionOnMissingFileName
    theFix.setSightingFile()
TypeError: setSightingFile() takes exactly 2 arguments (1 given)

======================================================================
ERROR: test300_010_ShouldIgnoreMixedIndentation (Navigation.test.FixTestCA03.TestFix)
parse sighting file that valid tags
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 612, in test300_010_ShouldIgnoreMixedIndentation
    theFix.setStarFile(self.starFileName)
AttributeError: Fix instance has no attribute 'setStarFile'

======================================================================
ERROR: test300_020_ShouldIgnoreMixedIndentation (Navigation.test.FixTestCA03.TestFix)
parse sighting file that has mixed indentation
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 624, in test300_020_ShouldIgnoreMixedIndentation
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_030_ShouldLogOneSighting (Navigation.test.FixTestCA03.TestFix)
log one valid adjusted altitude
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 639, in test300_030_ShouldLogOneSighting
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_040_ShouldLogMultipleSightingsInTimeOrder (Navigation.test.FixTestCA03.TestFix)
Log multiple stars that sorting
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 667, in test300_040_ShouldLogMultipleSightingsInTimeOrder
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_050_ShouldLogMultipleSightingsWithSameDateTime (Navigation.test.FixTestCA03.TestFix)
Log multiple stars that require sorting using body name
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 696, in test300_050_ShouldLogMultipleSightingsWithSameDateTime
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_060_ShouldHandleNoSightings (Navigation.test.FixTestCA03.TestFix)
ensure empty fix is handled without logging anything
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 721, in test300_060_ShouldHandleNoSightings
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_070_ShouldIgnoreExtraneousTags (Navigation.test.FixTestCA03.TestFix)
log information from recognized tags, ignore extraneous tags
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 743, in test300_070_ShouldIgnoreExtraneousTags
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_080_ShouldLogStarWithArtificialHorizon (Navigation.test.FixTestCA03.TestFix)
log adjusted altitude for artificial horizon
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 793, in test300_080_ShouldLogStarWithArtificialHorizon
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_080_ShouldLogStarWithNaturalHorizon (Navigation.test.FixTestCA03.TestFix)
log adjusted altitude for natural horizon
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 768, in test300_080_ShouldLogStarWithNaturalHorizon
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_090_ShouldLogStarWithDefaultSightingValues (Navigation.test.FixTestCA03.TestFix)
log adjusted altitude for star using default values
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 819, in test300_090_ShouldLogStarWithDefaultSightingValues
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_091_ShouldLogErrorOnMissingMandatoryTag (Navigation.test.FixTestCA03.TestFix)
Verify that missing mandatory tag was flagged as sighting error
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 844, in test300_091_ShouldLogErrorOnMissingMandatoryTag
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_092_ShouldLogErrorOnInvalidBody (Navigation.test.FixTestCA03.TestFix)
Verify that invalid body tag was flagged as sighting error
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 863, in test300_092_ShouldLogErrorOnInvalidBody
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_093_ShouldLogErrorOnInvalidDate (Navigation.test.FixTestCA03.TestFix)
Verify that invalid date tag was flagged as sighting error
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 882, in test300_093_ShouldLogErrorOnInvalidDate
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_094_ShouldLogErrorOnInvalidTime (Navigation.test.FixTestCA03.TestFix)
Verify that invalid time tag was flagged as sighting error
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 901, in test300_094_ShouldLogErrorOnInvalidTime
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_095_ShouldLogErrorOnInvalidObservation (Navigation.test.FixTestCA03.TestFix)
Verify that invalid observation tag was flagged as sighting error
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 920, in test300_095_ShouldLogErrorOnInvalidObservation
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_096_ShouldLogErrorOnInvalidHeight (Navigation.test.FixTestCA03.TestFix)
Verify that invalid height tag was flagged as sighting error
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 940, in test300_096_ShouldLogErrorOnInvalidHeight
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_097_ShouldLogErrorOnInvalidTemperature (Navigation.test.FixTestCA03.TestFix)
Verify that invalid temperature tag was flagged as sighting error
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 960, in test300_097_ShouldLogErrorOnInvalidTemperature
    theFix.setStarFile(self.starFileName)
AttributeError: Fix instance has no attribute 'setStarFile'

======================================================================
ERROR: test300_098_ShouldLogErrorOnInvalidPressure (Navigation.test.FixTestCA03.TestFix)
Verify that invalid pressure tag was flagged as sighting error
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 980, in test300_098_ShouldLogErrorOnInvalidPressure
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_099_ShouldLogErrorOnInvalidHorizon (Navigation.test.FixTestCA03.TestFix)
Verify that invalid horizon tag was flagged as sighting error
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 999, in test300_099_ShouldLogErrorOnInvalidHorizon
    theFix.setStarFile(self.starFileName)
AttributeError: Fix instance has no attribute 'setStarFile'

======================================================================
ERROR: test300_100_ShouldLogStarLatLon (Navigation.test.FixTestCA03.TestFix)
log geographical position with no interpolation of observation
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 1017, in test300_100_ShouldLogStarLatLon
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_110_ShouldLogStarLatLonWithInterpolation (Navigation.test.FixTestCA03.TestFix)
log geographical position
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 1044, in test300_110_ShouldLogStarLatLonWithInterpolation
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_910_ShouldRaiseExceptionOnNotSettingSightingsFile (Navigation.test.FixTestCA03.TestFix)
Raise exception on failure to set sighting file
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 1069, in test300_910_ShouldRaiseExceptionOnNotSettingSightingsFile
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_920_ShouldRaiseExceptionOnNotSettingStarFile (Navigation.test.FixTestCA03.TestFix)
Raise exception on failure to set star file
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 1083, in test300_920_ShouldRaiseExceptionOnNotSettingStarFile
    theFix.setAriesFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test300_930_ShouldRaiseExceptionOnNotSettingAriesFile (Navigation.test.FixTestCA03.TestFix)
Raise exception on failure to set aries file
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 1096, in test300_930_ShouldRaiseExceptionOnNotSettingAriesFile
    theFix.setStarFile(self.ariesFileName)
AttributeError: Fix instance has no attribute 'setStarFile'

======================================================================
ERROR: test400_030_ShouldSetValidAriesFileCA03 (Navigation.test.FixTestCA03.TestFix)
Set aries file and verify string is written to file
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 365, in test400_030_ShouldSetValidAriesFileCA03
    theFix.setAriesFile(testFile)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test400_910_ShouldRaiseExceptionOnNonStringFileNameCA03 (Navigation.test.FixTestCA03.TestFix)
Fail on setting aries file with non-string name
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 380, in test400_910_ShouldRaiseExceptionOnNonStringFileNameCA03
    theFix.setAriesFile(testFile)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test400_920_ShouldRaiseExceptionOnFileLengthErrorCA03 (Navigation.test.FixTestCA03.TestFix)
Fail on setting aries file with missing file prefix
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 391, in test400_920_ShouldRaiseExceptionOnFileLengthErrorCA03
    theFix.setAriesFile(testFile)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test400_930_ShouldRaiseExceptionOnNonXmlFile1CA03 (Navigation.test.FixTestCA03.TestFix)
Fail on setting aries  file with no txt extension
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 401, in test400_930_ShouldRaiseExceptionOnNonXmlFile1CA03
    theFix.setAriesFile(testFile)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test400_940_ShouldRaiseExceptionOnNonXmlFile2CA03 (Navigation.test.FixTestCA03.TestFix)
Fail on setting aries  file with txt name but not txt extension
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 411, in test400_940_ShouldRaiseExceptionOnNonXmlFile2CA03
    theFix.setAriesFile("txt")
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test400_950_ShouldRaiseExceptionOnMissingFileNameCA03 (Navigation.test.FixTestCA03.TestFix)
Fail on setting aries file with no name
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 421, in test400_950_ShouldRaiseExceptionOnMissingFileNameCA03
    theFix.setAriesFile()
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test400_960_SholdRaiseExceptionOnMissingFileCA03 (Navigation.test.FixTestCA03.TestFix)
Fail on setting aries file that does not exist
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 432, in test400_960_SholdRaiseExceptionOnMissingFileCA03
    theFix.setAriesFile(testFile)
AttributeError: Fix instance has no attribute 'setAriesFile'

======================================================================
ERROR: test500_030_ShouldSetValidStarFileCA03 (Navigation.test.FixTestCA03.TestFix)
Set star file and verify string is written to file
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 495, in test500_030_ShouldSetValidStarFileCA03
    theFix.setStarFile(testFile)
AttributeError: Fix instance has no attribute 'setStarFile'

======================================================================
ERROR: test500_910_ShouldRaiseExceptionOnNonStringFileNameCA03 (Navigation.test.FixTestCA03.TestFix)
Fail on setting star file with non-string name
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 510, in test500_910_ShouldRaiseExceptionOnNonStringFileNameCA03
    theFix.setStarFile(testFile)
AttributeError: Fix instance has no attribute 'setStarFile'

======================================================================
ERROR: test500_920_ShouldRaiseExceptionOnFileLengthErrorCA03 (Navigation.test.FixTestCA03.TestFix)
Fail on setting star file with missing file prefix
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 521, in test500_920_ShouldRaiseExceptionOnFileLengthErrorCA03
    theFix.setStarFile(testFile)
AttributeError: Fix instance has no attribute 'setStarFile'

======================================================================
ERROR: test500_930_ShouldRaiseExceptionOnNonXmlFile1CA03 (Navigation.test.FixTestCA03.TestFix)
Fail on setting star  file with no txt extension
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 531, in test500_930_ShouldRaiseExceptionOnNonXmlFile1CA03
    theFix.setStarFile(testFile)
AttributeError: Fix instance has no attribute 'setStarFile'

======================================================================
ERROR: test500_940_ShouldRaiseExceptionOnNonXmlFile2CA03 (Navigation.test.FixTestCA03.TestFix)
Fail on setting star  file with txt name but not txt extension
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 541, in test500_940_ShouldRaiseExceptionOnNonXmlFile2CA03
    theFix.setStarFile("txt")
AttributeError: Fix instance has no attribute 'setStarFile'

======================================================================
ERROR: test500_950_ShouldRaiseExceptionOnMissingFileNameCA03 (Navigation.test.FixTestCA03.TestFix)
Fail on setting star file with no name
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 551, in test500_950_ShouldRaiseExceptionOnMissingFileNameCA03
    theFix.setStarFile()
AttributeError: Fix instance has no attribute 'setStarFile'

======================================================================
ERROR: test500_960_SholdRaiseExceptionOnMissingFileCA03 (Navigation.test.FixTestCA03.TestFix)
Fail on setting star file that does not exist
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 562, in test500_960_SholdRaiseExceptionOnMissingFileCA03
    theFix.setStarFile(testFile)
AttributeError: Fix instance has no attribute 'setStarFile'

======================================================================
FAIL: test100_020_ShouldConstructFixWithDefaultFileCA03 (Navigation.test.FixTestCA03.TestFix)
Construct Fix with default log file name
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 101, in test100_020_ShouldConstructFixWithDefaultFileCA03
    self.fail("Major:  log file failed to create")
AssertionError: Major:  log file failed to create

======================================================================
FAIL: test100_030_ShouldConstructWithKeywordParmCA02 (Navigation.test.FixTestCA03.TestFix)
Construct Fix using named parameter
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 117, in test100_030_ShouldConstructWithKeywordParmCA02
    self.fail("Minor: " + str(e))
AssertionError: Minor: __init__() got an unexpected keyword argument 'logFile'

======================================================================
FAIL: test100_040_ShouldWriteFullPathToLogCA03 (Navigation.test.FixTestCA03.TestFix)
Construct Fix and ensure abspath is written to log file
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 132, in test100_040_ShouldWriteFullPathToLogCA03
    "Major:  first line of log is incorrect " + self.RANDOM_LOG_FILE)
AssertionError: Major:  first line of log is incorrect log79ab00b3b7a9.txt

======================================================================
FAIL: test100_050_ShouldConstructFixWithExistingFileCA02 (Navigation.test.FixTestCA03.TestFix)
Construct Fix and append to existing log file
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 149, in test100_050_ShouldConstructFixWithExistingFileCA02
    "Minor:  first line of log is incorrect " + self.RANDOM_LOG_FILE)
AssertionError: Minor:  first line of log is incorrect log29cf8c9735af.txt

======================================================================
FAIL: test100_910_ShouldRaiseExceptionOnFileNameLength (Navigation.test.FixTestCA03.TestFix)
Construct Fix with empty string
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 165, in test100_910_ShouldRaiseExceptionOnFileNameLength
    "Minor:  failure to check for log file name length")
AssertionError: Minor:  failure to check for log file name length

======================================================================
FAIL: test400_010_ShouldSetAriesFileWithOutKeywordParmCA03 (Navigation.test.FixTestCA03.TestFix)
Set aries file without keyword parm
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 340, in test400_010_ShouldSetAriesFileWithOutKeywordParmCA03
    self.fail("Minor: " + str(e))
AssertionError: Minor: Fix instance has no attribute 'setAriesFile'

======================================================================
FAIL: test400_020_ShouldConstructWithKeywordParmCA03 (Navigation.test.FixTestCA03.TestFix)
Set aries file with keyword parm
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 354, in test400_020_ShouldConstructWithKeywordParmCA03
    self.fail("Minor: " + str(e))
AssertionError: Minor: Fix instance has no attribute 'setAriesFile'

======================================================================
FAIL: test500_010_ShouldSetstarFileWithOutKeywordParmCA03 (Navigation.test.FixTestCA03.TestFix)
Set star file without keyword parm
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", line 470, in test500_010_ShouldSetstarFileWithOutKeywordParmCA03
    self.fail("Minor: " + str(e))
AssertionError: Minor: Fix instance has no attribute 'setStarFile'

======================================================================

    

def test50_020_ShouldConstructWithKeywordParmCA03 (self):
   pass#
#Set star file with keyword parm
  #File "C:\Users\Cesar\workspace\SoftProcTest\Navigation\test\FixTestCA03.py", 
  #line 484, in test500_020_ShouldConstructWithKeywordParmCA03
  #  self.fail("Minor: " + str(e))
#AssertionError: Minor: Fix instance has no attribute 'setStarFile'


'''