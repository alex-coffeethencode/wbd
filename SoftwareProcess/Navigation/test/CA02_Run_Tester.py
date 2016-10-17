
import Navigation.prod.Angle as Angle
import Navigation.prod.Fix as Fix

#from Navigation.prod.Angle import Angle
#from lib2to3.pgen2.tokenize import String
def main():
    myFix = Fix.Fix()
    myFix.setSightingFile("f4.xml")
    print("Start")
    approxPos = myFix.getSightings()
    
    print approxPos
    print("End")



main()