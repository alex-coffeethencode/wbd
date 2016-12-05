import unittest
import Navigation.prod.Angle as Angle
import math


class MyAngleTest(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

# ---------------
    # Just an inti test for confidance
    def test100_010_ShouldConstruct(self):
        self.assertIsInstance(Angle.Angle(), Angle.Angle)
    
    # Ta Notes
    def test200_010_setDegreesHasBad_Or_MissingReturn(self):
        myAngle = Angle.Angle()
        self.assertEquals(myAngle.setDegrees(50),50)
        
    def test200_020_setDeg_RaisesTypeError(self):
        expectedString = "Angle.setDegrees:"
        myAngle = Angle.Angle()
        #Should be value errror:
        with self.assertRaises(ValueError) as context:   
            myAngle.setDegrees("asdf")
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
        
        
    def test200_030_getDeg_Bad_Rounding(self):
        myAngle = Angle.Angle()
        myAngle.setDegrees(359.826)
        self.assertEquals(myAngle.getDegrees(),359.826)
        
    def test200_040_setDegAndMin_Bad_rounding(self):
        #? rounding tests? 
        myAngle = Angle.Angle()
        myAngle.setDegreesAndMinutes("719d49.56")
        self.assertEquals(myAngle.getDegrees(),359.826)
        
        
    # Throws an error on valid input?
    def test200_050_setDegAndMin_ThrowErrorOnValidInput(self):
        myAngle = Angle.Angle()
        myAngle.setDegreesAndMinutes("359d49.56")
        self.assertEquals(myAngle.getDegrees(),359.826)
        
    
    def test200_060_add_nothandleempty(self):
        expectedString = "Angle.add:"
        myAngle = Angle.Angle()
        with self.assertRaises(ValueError) as context:
            myAngle.add()
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
        
        
    def test200_070_sub_nothandleempty(self):
        expectedString = "Angle.sub:"
        
        myAngle = Angle.Angle()
        with self.assertRaises(ValueError) as context:
            myAngle.sub()
        
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
        
        
    def test200_080_comp_nothandleempty(self):
        expectedString = "Angle.compare:"
        
        myAngle = Angle.Angle()
        with self.assertRaises(ValueError) as context:
            myAngle.compare()
        
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
        
        
    def test200_090_comp_wrongresultreturned(self):
        myAngle = Angle.Angle()
        otherAngle = Angle.Angle()
        myAngle.setDegreesAndMinutes("10d0.0")
        otherAngle.setDegreesAndMinutes("20d0.0")
        self.assertEquals(myAngle.compare(otherAngle), -1)
        myAngle.add(otherAngle)
        self.assertEquals(myAngle.compare(otherAngle), 0)
        myAngle.add(otherAngle)
        self.assertEquals(myAngle.compare(otherAngle), 1)
        
    
    #~= 15 minutes
    
    
    
    #f1 = orig