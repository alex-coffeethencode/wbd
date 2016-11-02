''' 
    Angle:
        A class which creates, sets, and operates on Angles,
        According to project specifications.

    Baselined: Sept 4th, 2016 
    Modified: Oct 16th 2016
    @author:    Alex Schultz
 
'''

import math
from lib2to3.fixer_util import String, Dot

class Angle():
    degrees = 0
    minutes = 0
    
    def __init__(self):
        self.minutes = 0
        self.degrees = 0


    def setDegrees(self, degrees=0):
        try:

            while degrees < 0:
                degrees += 360
            degrees = (degrees) % 360            
            
            degInt = int(degrees)
            dif = degrees - degInt
            degrees = degInt
            
            self.degrees = degrees
            self.minutes = dif * 60
            
            return self.getDegrees()
        except:
            raise ValueError("Angle.setDegrees:  ValueError")

             
    def setDegreesAndMinutes(self, angleString):
        #try:    
        delimiter = 0
        try:
            delimiter = angleString.index('d')
        except:
            raise ValueError("Angle.setDegreesAndMinutes:  No delimiter 'd' found")
        if delimiter >= 1:
            degrees, minutes = angleString.split('d')            
            
            myBool = False
            try:
                dot = minutes.index('.')
                #if a period is found then check for only 1 decimal place
                if len(minutes) - 1 - dot > 1:
                    myBool = True
            except:
                pass
                #raise ValueError("Angle.setDegreesAndMinutes:  No delimiter '.' found")
            
            if myBool:
                raise ValueError("Angle.setDegreesAndMinutes:  No more than 1 decimal place")
                
            try:
                degrees = float(degrees)
                minutes = float(minutes)    
            except:
                raise ValueError("Angle.setDegreesAndMinutes:  Minf/Deg must be convertable to float")
                

            if minutes > 60:
                stub = minutes % 60.0
                degrees += (minutes - stub) / 60
                minutes = stub
                
            if minutes < 0:
                raise ValueError("Angle.setDegreesAndMinutes:  ValueError Minutes must be greater than 0")              
               
            if degrees < 0:
                minutes *= -1
                while degrees < 0:
                    degrees += 360
                  
            degrees = (degrees) % 360            
            degInt = int(degrees)
            dif = degrees - degInt
            if dif != 0:
                raise ValueError("Angle.setDegreesAndMinutes:  ValueError Degree must be an integer")
              
            self.minutes = minutes
            self.degrees = degrees
              
            return self.getDegrees()    
        else:
            raise ValueError("Angle.setDegreesAndMinutes:  No D is a delimter")
       
    
    def add(self, angle = "Not Set"):
        try:
            if type(angle) != type(Angle()):
                raise ValueError("Angle.add:  ValueError on input " )#+ str(angle.degrees) + " " + str(angle.minutes))
                        
            degIn = angle.degrees
            minIn = angle.minutes
            
            degrees = self.degrees + degIn
            minutes = self.minutes + minIn
            
            while degrees < 0:
                degrees += 360 

            if minutes >= 60:
                stub = minutes % 60
                degrees += (minutes - stub) / 60
                minutes = stub

            degrees = degrees % 360            
                                            
            self.minutes = minutes
            self.degrees = degrees
            
            return self.getDegrees()        
        except:
            raise ValueError("Angle.add:  ValueError  ") # + str(angle.degrees) + " " + str(angle.minutes))
        

    def subtract(self, angle = "Not Set"):
        try:
            if type(angle) != type(Angle()):
                raise ValueError("Angle.subtract:  ValueError on input " + str(angle.degrees) + " " + str(angle.minutes))
              
            degIn = angle.degrees
            minIn = angle.minutes
            
            degrees = self.degrees - degIn
            minutes = self.minutes - minIn
               
            if minutes >= 60:
                stub = minutes % 60
                degrees += (minutes - stub) / 60
                minutes = stub
            elif minutes < 0:
                while minutes < 0:
                    minutes += 60
                    degrees -= 1
            
            if degrees < 0:
                while degrees < 0:
                    degrees += 360 
                
            degrees %= 360         
                 
                
            self.minutes = minutes
            self.degrees = degrees
        
            return self.getDegrees()
        
        except:
            raise ValueError("Angle.subtract:  ValueError")
        
    
    def compare(self, angle = "Not Set"):
        try:
            if type(angle) != type(Angle()):
                raise ValueError("Angle.subtract:  ValueError on input " + str(angle.degrees) + " " + str(angle.minutes))
            
            if angle.getDegrees() < self.getDegrees():
                return 1
            elif angle.getDegrees() > self.getDegrees():
                return -1
            else:
                return 0
                                 
        except:
            raise ValueError("Angle.compare:  ValueError")
            
            
    def getString(self):
        if len(str(round(self.minutes))) == 3:
            minStr = str(round(self.minutes,1))
            return str(int(self.degrees)) + "d0" + minStr# / 60.0)

        return str(int(self.degrees)) + "d" + str(round(self.minutes,1))# / 60.0)
    
    def getDegrees(self):
        return float((self.degrees) +  round(self.minutes,1) / 60.0)
    