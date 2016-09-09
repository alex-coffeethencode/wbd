class Angle():
    
    degrees = 0
    minutes = 0
    
    def __init__(self):
        # No exceptions should be raised
        self.degrees = 0
        self.minutes = 0
        #?
        #self.angle = ...       set to 0 degrees 0 minutes
        
    def setDegrees(self, degrees = 0):
        try:
            #Throws type errors for strings
                #Note: Booleans are considered legal as numbers
            degrees += 0
            self.degrees = degrees
            
        except ValueError:
            print("Error: Degree input for setDegress is invalid")
            return "Error"
        except TypeError:
            print("Error: Make sure degree is either a float or int")
            return "Error"
    
    def setDegreesAndMinutes(self, degrees):
        delimiter = 0
        try:
            delimter = degrees.index('d')
            print(delimiter)
            
            
            
            self.degrees = degrees
            
            
        except ValueError:
            print("Error: Degree input for setDegress is invalid")
            return "Error"
        except TypeError:
            print("Error: Make sure degree is either a float or int")
            return "Error"
        
    
    def add(self, angle):
        pass
    
    def subtract(self, angle):
        pass
    
    def compare(self, angle):
        pass
    
    def getString(self):
        pass
    
    def getDegrees(self):
        pass