''' 
    Created on Sept 9th, 2016
 
    @author:    Alex Schultz
 
''' 
from Navigation.prod.Angle import Angle
from lib2to3.pgen2.tokenize import String

def MyTester():
    result = ""
    #result += "SetDegrees success ratio:           "  + str(testSetDegrees()) + "\n"
    result += "SetDegreesAndMinutes success ratio: "  + str(testSetDegreesAndMinutes()) + "\n"
    
    print result    
    #Done

def testAngle():
    myAngle = Angle()
    print("Testing testAngle")

# Should also compare to getDegrees
#Function:
#    Returns 0 (fail) if an error message was recieved during testing
def condSetDegrees(strIn):   
    errMsg = "Error"
    if strIn == errMsg :
        #if getDegrees = ,param -> return 1         : else return 0    
        return 0
    return 1

def testSetDegrees():
    myAngle = Angle()
    success = 0
    
    # Better testing approrah
    successArray = [12, 45.3, 12.1423145265, 0, -1234, True]
    for item in successArray:   
        # Default result is none, this allows 
        success += condSetDegrees(myAngle.setDegrees(item))
    
    # Python arrays fo no allow , , (a blank spot)   
    success += condSetDegrees(myAngle.setDegrees())
    
    
    failureArray = ["asdf", 'a', object]
    for item in failureArray:
        if not (condSetDegrees(myAngle.setDegrees(item))):
            success += 1
        
    #Done    
    
#Focus is on error message handling, getdegandmin focues on implemetentation
def testSetDegreesAndMinutes():
    myAngle = Angle()
    success = 0
    #Success

    successArray = ["45d10.1"]
    for item in successArray:
        success += condSetDegrees(myAngle.setDegreesAndMinutes(item))
        
    failureArray = []
    
    
    totalTests = len(failureArray) + len(successArray)    
    return (success/totalTests)
    
    
    
    #Done    
    
    
    
    
