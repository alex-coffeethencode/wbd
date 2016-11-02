
import unittest
import Navigation.prod.Fix as Fix
import math

import os.path

#20 min of test code writing with ~= 2 hours prep

#coding 1154 10/10

class Ca02_Test(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

#Individual Box Testing:

#m1 =  Fix() (The constructor)
    #Assert Valid contructor
    
        
    def test000_000_CheckAgaisntSampleProvided(self):
        file = "myLogFile.txt"
        
        os.remove(os.getcwd() + os.path.sep + file)

        a = open(file, "w+")
        a.close()
    
        
        myFix = Fix.Fix(file)
        myFix.setSightingFile("f.xml")
        a = myFix.getSightings()
        
        #myLog = open("myLogFile.txt")
        print a        
        
        # Line by line assertions:
        
    
    
     
    
    '''
    def test100_010_ShouldConstruct(self):
        self.assertIsInstance(Fix.Fix(), Fix.Fix)

    def test100_020_TestEmptyInput___ShouldCreateOutputDotText(self):
        myFix = Fix.Fix()
        self.assertEquals(myFix.logFile, "output.txt")
        #Need to assert that output.txt is created
        
    def test100_030_TestBadInput(self):
        expectedString = "Fix.Fix:"
        #Should be value errror:
        with self.assertRaises(ValueError) as context:   
            myFix = Fix.Fix("")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    
#    def test100_040_UnAppendableFile(self):
#        expectedString = "Fix.Fix:"
#        
 #       with self.assertRaises(ValueError) as context:   
 #           myFix = Fix.Fix("thisDoesntExistYet.txt")
 #       self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    
    def test100_050_LegalFile(self):
        filename = "myLogFile.txt"
        myFix = Fix.Fix(filename)
        self.assertEquals(myFix.logFile, filename)
#m2 = setSightingFile

    # Cut from testing
   # def test200_010_EmptyInput(self):
    #    expectedString = "Fix.setSightingFile:"
    #    myFix = Fix.Fix("text.txt")
    #    #Should be value error:
    #    with self.assertRaises(ValueError) as context:   
    #        myFix.setSightingFile()
    #    self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    
    def test200_020_BadExtension(self):
        expectedString = "Fix.setSightingFile:"
        myFix = Fix.Fix("text.txt")
        
        with self.assertRaises(ValueError) as context:   
            myFix.setSightingFile("text.txt")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    
    def test200_030_BadFilename_Good_Extension(self):
        expectedString = "Fix.setSightingFile:"
        myFix = Fix.Fix("text.txt")
        
        with self.assertRaises(ValueError) as context:   
            myFix.setSightingFile(".xml")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    
    # Cut from testing
    #def test200_040_CannotAppend(self):
    #    expectedString = "Fix.setSightingFile:"
    #    myFix = Fix.Fix("text.txt")
    #    
    #    with self.assertRaises(ValueError) as context:   
    #        myFix.setSightingFile("unAppendable.xml")
    #    self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    
    
    def test200_050_LegalFile(self):
        file = "test.txt"
        
        os.remove(os.getcwd() + os.path.sep + file)

        a = open(file, "w+")
        a.close()
        
        expectedString = "Fix.setSightingFile:"
        myFix = Fix.Fix(file)
        myFix.setSightingFile("f.xml")
        
        self.assertEquals(myFix.sightFile, "f.xml")
        
    
    # cutting, made Run_Tester for this exact purpose
 #   def test300_001_BadTestingPractice(self):
 #       myFix = Fix.Fix("myLogFile.txt")
 #       myFix.setSightingFile("f.xml")
 #       approxPos = myFix.getSightings()
        #No real test, trying ot confirm working without "run" ended up resorting to Run anyway
        
    
    # Another test where it should pass    
    def test300_010_F2_EmptyOrNoSighting(self):
        expectedString = "Fix.getSightings:"
        myFix = Fix.Fix("text.txt")
        myFix.setSightingFile("f2.xml")
        myFix.getSightings()
        
    
    def test300_020_F3_BadVarAsTag(self):
        expectedString = "Fix.getSightings:"
        myFix = Fix.Fix("text.txt")
        myFix.setSightingFile("f3.xml")
        myFix.getSightings()
        # No Assertion?
    
    def test300_030_F4_MissingTag(self):
        #MissingTempInSecondSighting
        expectedString = "Fix.getSightings:"
        myFix = Fix.Fix()
        
        with self.assertRaises(ValueError) as context:   
            myFix.setSightingFile("f4.xml")
            print("030 ------->" + str(myFix.getSightings()))
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    
    
    def test300_040_F5_MissingRequired(self):
        #Missing2ndObservationRequired
        
        expectedString = "Fix.getSightings:"
        myFix = Fix.Fix()
    
        with self.assertRaises(ValueError) as context:   
            myFix.setSightingFile("f5.xml")
            myFix.getSightings()
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    
    
    # 050 test internal tag stuff
#    def test300_051_F6_LeadingWhiteSpaceCut(self):
#        expectedString = "Fix.setSightingFile:"
#        myFix = Fix.Fix("text.txt")
#        #with self.assertRaises(ValueError) as context:   
#        myFix.setSightingFile("f6.xml")
#        myFix.getSightings()       
        # check  against logfile
        
        #self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
    
    
    
    
    # LSF = LegalSi
    #def test300_060_LegalSightingFile(self):
    #    expectedString = "Fix.setSightingFile:"
     #   myFix = Fix.Fix("myLogFile.txt")
#
 #       myFix.setSightingFile("f.xml")
  #      asdf = myFix.getSightings()
           
   #     myLog = open("myLogFile.txt", "r")
    #    firstLine = ""
     #   self.assertEqual(myLog[0], firstLine)
        
    
    
    
    
    #test 500 system
    
    # Test: make sure f.xml only writes once, f2 imeeditaly after
#    myFix = Fix.Fix("myLogFile.txt")
#    myFix.setSightingFile("f.xml")
#    approxPos = myFix.getSightings()
#    myFix.setSightingFile("f.xml")
#    approxPos = myFix.getSightings()
#    myFix.setSightingFile("f2.xml")
#    approxPos = myFix.getSightings()





    def test000_001_SandBoxTesting(self):
        file = "sandboxTesting.txt"
        os.remove(os.getcwd() + os.path.sep + file)

        a = open(file, "w+")
        a.close()
        
        lineOne = "LOG:\t2016-10-01 10:01:09-06:00\tStart of log\n"
        lineTwo = "LOG:\t2016-10-01 10:01:10-06:00\tStart of sighting file:  f.xml"
        lineThr = "LOG:\t2016-10-01 10:01:10-06:00\tAldebaran   2016-03-01   23:30:01   15d01.5"
        lineFor = "LOG:\t2016-10-01 10:01:10-06:00\tPeacock   2016-03-02   00:05:05   45d11.9"
        lineFiv = "LOG:\t2016-10-01 10:01:10-06:00\tEnd of sighting file:  f.xml"

        
        myFix = Fix.Fix(file)
        myFix.setSightingFile("f7.xml")
        a = myFix.getSightings()
        
        myLog = open("myLogFile.txt")
        lineArray = myLog.readlines()
        
        #self.assertEquals(lineArray[0], lineOne)
        #self.assertEquals(lineArray[1][0:-1], lineTwo)
        #self.assertEquals(lineArray[2][0:-1], lineThr)
        #self.assertEquals(lineArray[3][0:-1], lineFor)
        self.assertEquals(lineArray[4][0:-1], lineFiv)

'''
   