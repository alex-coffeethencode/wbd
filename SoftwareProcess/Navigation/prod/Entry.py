''' 
    Entry is a refactored class from Fix.getSighting
    
    Baselined: Nov 30th, 2016 
    Modified: Dec 3rd th 2016
    @author:    Alex Schultz
 
'''

import math
from lib2to3.fixer_util import String, Dot
import Navigation.prod.Angle as Angle
from operator import itemgetter
import sha
from pip._vendor.pkg_resources import working_set

#+12
class Entry():
    fullyAdjustedAlt = False
    validEntry = False
    body = "---"
    date = "---"
    time = "---"
    observation = "---"

    height = 0
    temp = 72
    pressure = 1010
    horizen = "Natural"
    
    geoPos = "---"
    geoLat = "---"
    geoLong = "---"
    
    def __init__(self):
        self.validEntry = False
#5     
    def createEntry(self, xmlFormat):
        allVar = ["height", "temperature", "pressure", "horizon", "body", "date", "time", "observation"]

        #Must search by tag name. This process is more roundabout, but implemented befre disvocery of xml tree 
        #reqVar == tag name
        for item in allVar:
            var = xmlFormat.getElementsByTagName(item)
            #var = xmlFormat.getElementsByTagName(item)
            if len(var) > 0:
                var = var[0]
                value = (var.firstChild.nodeValue).encode('ascii', 'ignore')

                self.setValue(item, value)
        returnValue = self.validateEntry()
        return returnValue
#2        
    def setValue(self, item, value):
        #value = value.strip()
        if item == "body":
            # check to see if valid star?
            self.body = value
        elif item == "date":
            if self.checkDateFormat(value):
                self.date = value
        elif item == "time":
            if self.checkTimeFormat(value):
                self.time = value
        elif item == "observation":
            if self.checkAngleFormat(value):
                self.observation = value
        elif item == "height":
            value = float(value)
            if value >= 0:
                self.height = value
        elif item == "temp":
            value = int(value)
            if value > -20 and value < 120:
                self.temp = value
        elif item == "pressure":
            self.pressure = value
        elif item == "horizen":
            if self.horizen.lower() == "natural" or self.horizen.lower() == "artificial" :
                self.horizen = value
 #3  
    def checkDateFormat(self, dateIn):
        try:
            y,m,d = dateIn.split("-")
        except:
            return False
        m = int(m)
        d = int(d)
        
        if len(y) != 4:
            return False
        
        if not m >= 0 and not m <= 12:
            return False
        
        if not d >= 0 and not d <= 31:
            return False
        return True
    #2
    def changeDateFormat(self, dateIn):
        #m,d,yr = dateIn.split("/")
        #newDate = "20" + yr + "-" + m + "-" + d 
        yr,d,m  = dateIn.split("-")
        newDate =  "" + d + "/" + m + "/" + yr[2:] 
        return newDate
#2
    def checkTimeFormat(self, timeIn):
        try:
            h,m,s = timeIn.split(":")
        except:
            return False
            #  print ("ERROR FOUND ****************    " + dateIn)
        m = int(m)
        s = int(s)
        h = int(h)
    
        if not m >= 0 and not m <= 60:
            return False
        if not s >= 0 and not s <= 60:
            return False
        if not h >= 0 and not h <= 24:
            return False
        return True
  #1     
    def validateEntry(self):
        if self.body == "---" or self.date == "---" or self.time == "---" or self.observation == "---":
            self.validEntry = False
        else:
            self.validEntry = True
        
        return self.validEntry
        
#0        
    def checkAngleFormat(self, stringIn):
        myAngle = Angle.Angle()
        try:
            result = myAngle.setDegreesAndMinutes(stringIn)
        except:
            return False
        if isinstance(result, ValueError):
            return False
        return True
#0
    def validBody(self):
        if self.body == "---":
            return False
        else:   
            return True
    #12
    #Calc returns rather than raises ValueError so that file can be appeneded?
    def calcAdjAlt(self):
        sampAngle = Angle.Angle()
        if self.observation == "---":
            self.fullyAdjustedAlt = False
            return ValueError("Fix.setSightingFile:  error inobservartion")
        
        sampAngle.setDegreesAndMinutes(self.observation)
        otherAngle = Angle.Angle()
            
        if sampAngle.getDegrees() < 0.1:
            
            self.fullyAdjustedAlt = False
            return ValueError("Fix.setSightingFile:  Must be greater than 0.1")
       
        dip = 0
        refraction = 0
       
        try:
            if self.horizen.lower() == "natural":
                dip = -0.97/ 60
                dip = dip * math.sqrt(float(self.height))
                
        except:
            
            self.fullyAdjustedAlt = False
            return ValueError("Fix.setSightingFile:  Problems in calc dip ")
       
        try:    
    #        refraction = ( -0.00452 * pressure ) / ( 273 + celsius( temperature ) ) / tangent( altitude )                    
            a = (-0.00452 * float(self.pressure))
            b = (273 + ((float(self.temp) - 32) / 1.8))
            c = math.tan(math.radians(sampAngle.getDegrees()))
            
            refraction = a / b / c
            
        except:
            self.fullyAdjustedAlt = False
            return ValueError("Fix.setSightingFile:  Problems in calc  refraction")
       
        try:        
            otherAngle.setDegrees(dip + refraction)
            sampAngle.add(otherAngle)
            self.fullyAdjustedAlt = sampAngle
            return sampAngle        
        except:
            self.fullyAdjustedAlt = False
            return ValueError("Fix.setSightingFile:  Problems adding angles")
        return ValueError("Fix.setSightingFile:  Problems adding angles")
           
#6
    def calcGeo(self, gha1,gha2, sha):
        try:
            gha1.getDegrees()
            sha.getDegrees()
            gha2.getDegrees()
        except:
            raise ValueError("Fix.writeToLog:  ValueError on type of input " )

        aries = Angle.Angle()


        min = int(self.time[3:5])
        s = int(self.time[6:])

        s = 60 * min + s
        
        dif = gha2.subtract(gha1) * (s/3600.0)
        aries.setDegrees(dif + gha1.getDegrees())
        aries.add(sha)
        
        return aries       
    
    #14
    #also calcs azimuth 
    def adjPos(self, geoLong, assLong, assLat, geoLat, mult = 1):        
        lha = geoLong
        lha.add(assLong)
        
        sl1 = math.sin(math.radians(geoLat.getDegrees()))
        sl2 = math.sin(math.radians(assLat.getDegrees()))
        sl = sl1 * sl2
        
        cl1 = math.cos(math.radians(geoLat.getDegrees()))
        cl2 = math.cos(math.radians(assLat.getDegrees()))
        
        coslha = math.cos(math.radians(lha.getDegrees())) 
        cl = coslha * cl1 * cl2* mult
        
        id = sl + cl
        
        corAlt = math.asin(id)
        corAltAng = lha
        
        actDeg = math.degrees(corAlt)
        
        corAltAng.setDegrees(actDeg)
        
        ### azi
        azimuth = Angle.Angle()
        numerator = sl1-(sl2 * id)
        
        denominator = (cl2 * math.cos(corAlt) * mult)
        
        res = numerator / denominator
        res = math.acos(res)
        azimuth.setDegrees(math.degrees(res))

        return (corAltAng,azimuth)
        