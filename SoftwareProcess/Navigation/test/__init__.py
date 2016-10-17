''' 
    Test acts as my testing ground and sandbox.
        As code functionality was written after/during testing,
        I used my tests to show any bugs in my code.
    Baselined: Sept 4th, 2016 
    Modified: Sept 11th 2016
    @author:    Alex Schultz
 
'''


import Navigation.prod.Angle as Angle
import Navigation.prod.Fix as Fix

#from Navigation.prod.Angle import Angle
#from lib2to3.pgen2.tokenize import String
def main():
    myFix = Fix.Fix("myLogFile.txt")
    myFix.setSightingFile("f.xml")

    print("Start")
    approxPos = myFix.getSightings()
    print("End")


main()


def MyTester():
    #testAngle()
    
    #result = ""
    #result += "SetDegrees success ratio:           "  + str(testSetDegrees()) + "\n"
    #result += "SetDegreesAndMinutes success ratio: "  + str(testSetDegreesAndMinutes()) + "\n"
    
    testSetAndGetAngles()
    testAddAndSubAngles()
    
    #print result    
    
    
    
    
    
    
    
def testSetDegrees():
    success = 0
    
    # Better testing approrah
    successArray = [12, 45.3, 12.1423145265, 0, -1234, -12.46, True]
    for item in successArray:   
        # Default result is none, this allows 
        
        myAngle = Angle.Angle()
        #success += condSetDegrees(myAngle.setDegrees(item))
    
    # Python arrays fo no allow , , (a blank spot)   
    #success += condSetDegrees(myAngle.setDegrees())   
    
    failureArray = ["asdf", 'a', object]
    for item in failureArray:
        myAngle = Angle.Angle()
        #if not (condSetDegrees(myAngle.setDegrees(item))):
         #   success += 1
        
    #Done    

    totalTests = len(failureArray) + len(successArray)    
    return (success/totalTests)
    
    
#Focus is on error message handling, getdegandmin focues on implemetentation
def testSetDegreesAndMinutes():
  
    success = 0
    #Success

    successArray = ["45d10.1","45d10","0d0","0d0.1","700d1","700d61","-10d0","-10d1"]
    expOutput = []
    for item in successArray:    
        myAngle = Angle.Angle()
        #success += condSetDegrees(myAngle.setDegreesAndMinutes(item))
        
    failureArray = ["d10.0","10d","10","0.1d0","0d-10", "0d5.44", "xd10", "10dy", "10:30", ""]
    
    totalTests = len(failureArray) + len(successArray)    
    return (success/totalTests)
    
    #Done    
    
    
    
def testSetAndGetAngles():
    print("Get/Set Deg to Deg: ")
    successArray = [0, 359, 360, 361, 719, 100.5, 100.123, -43.5, -1]
    expectedOutput = [0, 359, 0, 1, 359, 100.5, 100.1, 316.5, 359]
    ctr = 0
    failed = 0
    for item in successArray:
        myAngle = Angle.Angle()
        myAngle.setDegrees(item)
        if expectedOutput[ctr] != myAngle.getDegrees():
            print (str(item) + " \t " + str(expectedOutput[ctr])  + " \t  "  + str(myAngle.getDegrees()))
            failed += 1
        ctr += 1
    print ("Total Tests: " + str(ctr) + " Failures: " + str(failed) + "\n")
    
    
    print("Get/Set Str to Str: ")
    successArray = ["0d0", "359d0", "360d0", "361d0", "719d0", "100d30"]
    expectedOutput = ["0d0.0", "359d0.0", "0d0.0", "1d0.0", "359d0.0", "100d30.0"]
    ctr = 0
    failed = 0
    for item in successArray:
        myAngle = Angle.Angle()
        myAngle.setDegreesAndMinutes(item)
        if expectedOutput[ctr] != myAngle.getString():
            print (str(item) + " \t " + str(expectedOutput[ctr])  + " \t  "  + str(myAngle.getString()))
            failed += 1
        ctr += 1
    print ("Total Tests: " + str(ctr) + " Failures: " + str(failed) + "\n")
    

    print("Get/Set Deg to Str: ")
    successArray = [0, 359, 360.5, -719.5]
    expectedOutput = ["0d0.0", "359d0.0", "0d30.0", "0d30.0"]
    ctr = 0
    failed = 0
    for item in successArray:
        myAngle = Angle.Angle()
        myAngle.setDegrees(item)
        if expectedOutput[ctr] != myAngle.getString():
            print (str(item) + " \t " + str(expectedOutput[ctr])  + " \t  "  + str(myAngle.getString()))
            failed += 1
        ctr += 1
    print ("Total Tests: " + str(ctr) + " Failures: " + str(failed) + "\n")
    

    print("Get/Set Str to Deg: ")
    successArray = ["0d0.0", "359d0.0", "360d30.0"]
    expectedOutput = [0, 359, 0.5]
    ctr = 0
    failed = 0
    for item in successArray:
        myAngle = Angle.Angle()
        myAngle.setDegreesAndMinutes(item)
        if expectedOutput[ctr] != myAngle.getDegrees():
            print (str(item) + " \t " + str(expectedOutput[ctr])  + " \t  "  + str(myAngle.getDegrees()))
            failed += 1
        ctr += 1
    print ("Total Tests: " + str(ctr) + " Failures: " + str(failed) + "\n")
    

    #successArray = ["45d10.1","45d10","0d0","0d0.1","700d1","700d61","-10d0","-10d1"]
     
     
    # Designed to Fail from customer needs
    print("Failing Get/Set Str to Str: ")
    failureArray = ["d10.0","10d","10","0.1d0","0d-10", "0d5.44", "xd10", "10dy", "10:30", ""]
    ctr = 0
    failed = 0
    for item in failureArray:
        myAngle = Angle.Angle()
        try:
            print(str(item) + "  " + str(myAngle.setDegreesAndMinutes(item)))
            
        except ValueError:
            failed += 1
        ctr += 1
    print ("Total Tests: " + str(ctr) + " Failures: (thats actually good)" + str(failed) + "\n")
    



#    myAngle = Angle.Angle()
#    myAngle.setDegrees(100.5)
#    print(myAngle.getDegrees())
#    print(myAngle.getString())

def testAddAndSubAngles(): 
    print("Add Deg to Deg: ")
    anglesA = [0,360, -720,200,12.5, -7]
    anglesB = [0,360, -720,100,12.6, 8]
    expectedOutput = [0,0,0,300,25.1, 1]
    
    ctr = 0
    failed = 0
    for pos in anglesA:
        A = Angle.Angle()
        B = Angle.Angle()
        
        A.setDegrees(anglesA[ctr])
        B.setDegrees(anglesB[ctr])
        
        C= A.add(B)
        
        if expectedOutput[ctr] != C:
            print (str(A.getDegrees) + " \t" +  str(B.getDegrees()) + " \t Exp: " + str(expectedOutput[ctr]) + "  Res: "  + str(C))
            failed += 1
        ctr += 1
    print ("Total Tests: " + str(ctr) + " Failures: " + str(failed) + "\n")





    print("Sub Deg to Deg: ")
    anglesA = [0,360, -720,200,12.5, -7]
    anglesB = [0,360, -720,100,12.6, 8]
    expectedOutput = [0,0,0,100,359.9, 345]
    
    ctr = 0
    failed = 0
    for pos in anglesA:
        A = Angle.Angle()
        B = Angle.Angle()
        
        A.setDegrees(anglesA[ctr])
        B.setDegrees(anglesB[ctr])
        
        C= A.subtract(B)
        
        if expectedOutput[ctr] != C:
            print (str(A.getDegrees) + " \t" +  str(B.getDegrees()) + " \t Exp: " + str(expectedOutput[ctr]) + "  Res: "  + str(C))
            failed += 1
        ctr += 1
    print ("Total Tests: " + str(ctr) + " Failures: " + str(failed) + "\n")






    print("Compare Deg to Deg: ")
    anglesA = [0,360, -720,200,12.5, -7]
    anglesB = [0,360, -720,100,12.6, 8]
    expectedOutput = [0,0,0,-1,1, -1]
        
    ctr = 0
    failed = 0
    for pos in anglesA:
        A = Angle.Angle()
        B = Angle.Angle()
        
        A.setDegrees(anglesA[ctr])
        B.setDegrees(anglesB[ctr])
        
        C= A.compare(B)
        
        if expectedOutput[ctr] != C:
            print (str(A.getDegrees) + " \t" +  str(B.getDegrees()) + " \t Exp: " + str(expectedOutput[ctr]) + "  Res: "  + str(C))
            failed += 1
        ctr += 1
    print ("Total Tests: " + str(ctr) + " Failures: " + str(failed) + "\n")












#Modified for testing 
def modCustomerTrialRun():
    # ---------- constructor ----------
    # Instantiate angles
    angle1 = Angle.Angle()
    angle2 = Angle.Angle()
    angle3 = Angle.Angle()
    angle4 = Angle.Angle()
    # ---------- set ----------
    angle1Degrees = angle1.setDegreesAndMinutes("45d0.0")   #angle1Degrees should be 45.0
    angle2Degrees = angle2.setDegrees(degrees=-19.5)        #angle2Degrees should be 340.5
    angle3Degrees = angle3.setDegreesAndMinutes("0d30.0")   #angle3Degrees should be 0.5
  
    #print(str(angle1.getDegrees()) + " Should be 45.0")
    #print(str(angle2.getDegrees()) + " Should be 340.5")  
   # print (angle3Degrees)
   # print(str(angle3.getDegrees()) + " Should be .5")
   # print(str(angle3.getString()) + " Should be .5")

    
    # Attempts to set an invalid value should result
    # in a ValueError exception bearing a diagnostic message
    
    try:
        invalidAngle = angle2.setDegreesAndMinutes("")
    except ValueError as raisedException:
        diagnosticString = raisedException.args[0]
        print(str(diagnosticString) + " <- LEGAL")
    
    # ---------- add ----------
    # Add angle2 to angle1; save result in angle1; return result as degrees
    # 45d0 + 340d30 = 385d30 = 25d30 = 25.5 degrees
    addedDegrees1 = angle1.add(angle2)  #addedDegress1 should be 45d0 + 340d30 = 385d30 = 25d30 = 25.5 
    # Add angle3 to angle2; save result in angle2; return result as degrees
    addedDegrees3 = angle2.add(angle3)  #addedDegrees should be 340d30 + 0d30 = 340d60 = 341d0 = 341.0
    
    print("Adding Test")
    print(str(addedDegrees1) + "addedDegress1 should be 45d0 + 340d30 = 385d30 = 25d30 = 25.5")
    print(str(addedDegrees3) + "addedDegrees should be 340d30 + 0d30 = 340d60 = 341d0 = 341.0")
    
    
    
    # Attempts to pass a parm that is not an instance of Angle
    # should result in a ValueError exception bearing a diagnostic message.
    try:
        angle1.add("42d0")
    except ValueError as raisedException:
        diagnosticString = raisedException.args[0]
        print(str(diagnosticString) + " <- LEGAL")
    
    # ---------- subtract ----------
    # Subtract angle1 from angle4; save result in angle4; return result as degrees
    subtractedDegrees = angle4.subtract(angle1) #subtracted degrees should be 0d0 - 25d30 = -25d30 = 334d30= 334.5
    print(str(subtractedDegrees) + "  subtracted degrees should be 0d0 - 25d30 = -25d30 = 334d30= 334.5")

    
    # Attempts to pass a parm that is not an instance of Angle
    # should result in a ValueError exception bearing a diagnostic message.
    print("Subtraction")
    
    try:
        angle1.subtract(0)
    except ValueError as raisedException:
        diagnosticString = raisedException.args[0]
        print(str(diagnosticString) + " <- LEGAL")

    # ---------- compare ----------
    # Compare angle2 to angle1.  Return -1 if angle1 is less than angle2,
    # +1 if angle1 is greater than angle2
    # 0 if angle1 is equal to angle2
    angle1.setDegrees(45.0)
    angle2.setDegrees(45.1)
    result = angle1.compare(angle2) #result should be -1
    print("Compare: (-1) " + str(result))
    
    # Attempts to pass a parm that is not an instance of Angle
    # should result in a ValueError exception bearing a diagnostic message
    try:
        angle1.compare(42.0)
    except ValueError as raisedException:
        diagnosticString = raisedException.args[0]
        print(str(diagnosticString) + " <- LEGAL")
    
    
    
    # ---------- getString ----------
    angle1String = angle1.getString()   #angle1String should be "45d0.0"
    angle2String = angle2.getString()   #angle2String should be "45d6.0"
#    print(str(angle1String) + "  45d0.0")
#    print(str(angle2String) + "  45d6.0")
    
    angle3.setDegrees(45.123)
    angle3String = angle3.getString()   #angle3String should be "45d7.4"
#    print(str(angle3String) + "  45d7.4")
    
    
    
    # ---------- getDegrees ----------
    angle1Degrees = angle1.getDegrees()   #angle1String should be 45.0
    angle2Degress = angle2.getDegrees()   #angle2String should be 45.1
    angle3Degrees = angle3.getDegrees()   #angle3String should be 45.1
    
    '''
    print(angle1.getDegrees())
    print(angle2.getDegrees())
    print(angle3.getDegrees())
    '''
    
    
    #Done















def customerTrialRun():
    # ---------- constructor ----------
    # Instantiate angles
    angle1 = Angle.Angle()
    angle2 = Angle.Angle()
    angle3 = Angle.Angle()
    angle4 = Angle.Angle()
    
    
    
    # ---------- set ----------
    angle1Degrees = angle1.setDegreesAndMinutes("45d0.0")   #angle1Degrees should be 45.0
    angle2Degrees = angle2.setDegrees(degrees=-19.5)        #angle2Degrees should be 340.5
    angle3Degrees = angle3.setDegreesAndMinutes("0d30.0")   #angle3Degrees should be 0.5
    
    # Attempts to set an invalid value should result
    # in a ValueError exception bearing a diagnostic message
    try:
        invalidAngle = angle2.setDegreesAndMinutes("")
    except ValueError as raisedException:
        diagnosticString = raisedException.args[0]
    
    
    # ---------- add ----------
    # Add angle2 to angle1; save result in angle1; return result as degrees
    # 45d0 + 340d30 = 385d30 = 25d30 = 25.5 degrees
    addedDegrees1 = angle1.add(angle2)  #addedDegress1 should be 45d0 + 340d30 = 385d30 = 25d30 = 25.5 
    # Add angle3 to angle2; save result in angle2; return result as degrees
    addedDegrees3 = angle2.add(angle3)  #addedDegrees should be 340d30 + 0d30 = 340d60 = 341d0 = 341.0
    
    # Attempts to pass a parm that is not an instance of Angle
    # should result in a ValueError exception bearing a diagnostic message.
    try:
        angle1.add("42d0")
    except ValueError as raisedException:
        diagnosticString = raisedException.args[0]
    
    
    # ---------- subtract ----------
    # Subtract angle1 from angle4; save result in angle4; return result as degrees
    subtractedDegrees = angle4.subtract(angle1) #subtracted degrees should be 0d0 - 25d30 = -25d30 = 334d30= 334.5
    
    # Attempts to pass a parm that is not an instance of Angle
    # should result in a ValueError exception bearing a diagnostic message.
    try:
        angle1.subtract(0)
    except ValueError as raisedException:
        diagnosticString = raisedException.args[0]
    
    
    
    # ---------- compare ----------
    # Compare angle2 to angle1.  Return -1 if angle1 is less than angle2,
    # +1 if angle1 is greater than angle2
    # 0 if angle1 is equal to angle2
    angle1.setDegrees(45.0)
    angle2.setDegrees(45.1)
    result = angle1.compare(angle2) #result should be -1
    
    
    # Attempts to pass a parm that is not an instance of Angle
    # should result in a ValueError exception bearing a diagnostic message
    try:
        angle1.compare(42.0)
    except ValueError as raisedException:
        diagnosticString = raisedException.args[0]
    
    
    
    
    # ---------- getString ----------
    angle1String = angle1.getString()   #angle1String should be "45d0.0"
    angle2String = angle2.getString()   #angle2String should be "45d6.0"
    angle3.setDegrees(45.123)
    angle3String = angle3.getString()   #angle3String should be "45d7.4"
    
    
    
    # ---------- getDegrees ----------
    angle1Degrees = angle1.getDegrees()   #angle1String should be 45.0
    angle2Degress = angle2.getDegrees()   #angle2String should be 45.1
    angle3Degrees = angle3.getDegrees()   #angle3String should be 45.1
    
    #Done














## Standalone run:
#main()

