import unittest
import Navigation.prod.TCurve as T
import math


class TCurveTest(unittest.TestCase):

    def setUp(self):
        self.nominalN  = 4
        self.nominalT = 1.4398

    def tearDown(self):
        pass

# -----------------------------------------------------------------------
# ---- Acceptance Tests
# 100 constructor
#    Desired level of confidence:    boundary value analysis
#    Input-output Analysis
#        inputs:      n ->    integer .GE. 2 and .LT. 30  mandatory, unvalidated
#        outputs:    instance of TCurve
#    Happy path analysis:    
#        n:      nominal value    n=4
#                low bound        n=2
#                high bound       n=29
#    Sad path analysis:
#        n:      non-int n          n="abc"
#                out-of-bounds n    n=1; n=30
#                missing n
#
# Happy path 
    def test100_010_ShouldConstruct(self):
        self.assertIsInstance(T.TCurve(self.nominalN), T.TCurve)
        # additional tests are for boundary value coverage
        self.assertIsInstance(T.TCurve(2), T.TCurve)
        self.assertIsInstance(T.TCurve(29), T.TCurve)
        
# Sad path  
    def test100_910_ShouldRaiseExceptionNonintegerN(self):
        expectedString = "TCurve.__init__:"
        with self.assertRaises(ValueError) as context:
            T.TCurve("abc")                           
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])    

    def test100_920_ShouldRaiseExceptionOnBelowBoundN(self):
        expectedString = "TCurve.__init__:"
        with self.assertRaises(ValueError) as context:
            T.TCurve(1)                           
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
        
    def test100_930_ShouldRaiseExceptionOnAboveBoundN(self):
        expectedString = "TCurve.__init__:"
        with self.assertRaises(ValueError) as context:
            T.TCurve(30)                           
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])        
        
    def test100_940_ShouldRaiseExceptionOnMissingN(self):
        expectedString = "TCurve.__init__:"
        with self.assertRaises(ValueError) as context:
            T.TCurve()                           
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)]) 
   
   
   
   
   
   
   
   


        
# 600 p
#    Desired level of confidence:    boundary value analysis
#    Input-output Analysis
#        inputs:      t ->    float > 0.0, mandatory, unvalidated
#                     tails -> integer, 1 or 2, optional, defaults to 1
#        outputs:    float .GT. 0 .LE. 1.0
#    Happy path analysis:    
#        t:      nominal value    t=1.4398
#                low bound        t>0.0
#        tails:  value 1          tails = 1
#                value 2          tails = 2
#                missing tails
#        output:
#                The output is an interaction of t x tails x n:
#                    nominal t, 1 tail
#                    nominal t, 2 tails
#                    low n, low t, 1 tail
#                    low n, low t, 2 tails
#                    high n, low t, 1 tail
#                    high n, low t, 2 tails
#                    low n, high t, 1 tail
#                    low n, high t, 2 tails
#                    high n, high t, 1 tail
#                    high n, high t, 2 tails
#    Sad path analysis:
#        t:      missing t          
#                out-of-bounds n  t<0.0
#                non-numeric t    t="abc"
#        tails:  invalid tails    tails = 3
#
# Happy path


        
    def test600_010ShouldCalculateNominalCase1Tail(self):
        myT = T.TCurve(7)
        self.assertAlmostEquals(myT.p(1.8946, 1), .95, 3)
        
    def test600_020ShouldCalculateNominalCase2Tail(self):
        myT = T.TCurve(7)
        self.assertAlmostEquals(myT.p(1.8946, 2), .90, 3)

    def test600_030ShouldCalculateLowNLowT1TailEdgeCase(self):
        myT = T.TCurve(3)
        self.assertAlmostEquals(myT.p(0.2767, 1), 0.6, 3)   
             
    def test600_040ShouldCalculateLowNLowT2TailEdgeCase(self):
        myT = T.TCurve(3)
        self.assertAlmostEquals(myT.p(0.2767, 2), 0.2, 3)        

    def test600_050ShouldCalculateHighNLowT1TailEdgeCase(self):
        myT = T.TCurve(20)
        self.assertAlmostEquals(myT.p(0.2567, 1), 0.6, 3)
            
    def test600_060ShouldCalculateHighNLowT2TailEdgeCase(self):
        myT = T.TCurve(20)
        self.assertAlmostEquals(myT.p(0.2567, 2), 0.2, 3)    

    def test600_070ShouldCalculateLowNHighT1EdgeCase(self):
        myT = T.TCurve(3)
        self.assertAlmostEquals(myT.p(5.8409, 1), .995, 3)
        
    def test600_080ShouldCalculateLowNHighT2EdgeCase(self):
        myT = T.TCurve(3)
        self.assertAlmostEquals(myT.p(5.8409, 2), .99, 3)
        
    def test600_090ShouldCalculateHighHighT1TailEdgeCase(self):
        myT = T.TCurve(20)
        self.assertAlmostEquals(myT.p(2.8453, 1), .995, 3)
        
    def test600_100ShouldCalculateHighHighT2TailEdgeCase(self):
        myT = T.TCurve(20)
        self.assertAlmostEquals(myT.p(2.8453, 2), .99, 3)

# Sad path
    def test600_910ShouldRaiseExceptionOnMissingT(self):
        expectedString = "TCurve.p:"
        myT = T.TCurve(self.nominalN)
        with self.assertRaises(ValueError) as context:
            myT.p(tails=1)                       
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)]) 
        
    def test600_920ShouldRaiseExceptionOnOutOfBoundsT(self):
        expectedString = "TCurve.p:"
        myT = T.TCurve(self.nominalN)
        with self.assertRaises(ValueError) as context:
            myT.p(t= -1, tails=1)                       
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)]) 
        
    def test600_930ShouldRaiseExceptionOnNonNumericT(self):
        expectedString = "TCurve.p:"
        myT = T.TCurve(self.nominalN)
        with self.assertRaises(ValueError) as context:
            myT.p(t= "abc", tails=1)                       
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)]) 
            
    def test600_930ShouldRaiseExceptionInvalidTails(self):
        myT = T.TCurve(self.nominalN)
        with self.assertRaises(ValueError) as context:
            myT.p(t=self.nominalT, tails=0)

#--------------------------------------------------------------------
# Architecture:
#    p -> calculateConstant
#    p -> integrate
#    calculateConstant -> gamma
#    integrate -> f
#
#---- Unit tests      
#
# 200 gamma
#     Analysis
#        inputs:
#            x ->  float mandatory validated
#     Happy path:
#            x:    termination condition    x=1
#                  termination condition    x=1/2
#                  nominal value            x=5
#                  nominal value            x=5/2
#     Sad path:
#            none ... x is pre-validated
#
    def test200_010_ShouldReturnUpperTerminationCondition(self):
        myT = T.TCurve(self.nominalN)
        self.assertEquals(myT.gamma(1), 1)
        
    def test200_020_ShouldReturnLowerTerminationCondition(self):
        myT = T.TCurve(self.nominalN)
        self.assertEquals(myT.gamma(1.0 / 2.0), math.sqrt(math.pi))
        
    def test200_030_ShouldWorkOnIntegerX(self):
        myT = T.TCurve(self.nominalN)
        self.assertEquals(myT.gamma(5), 24)
        
    def test200_030_ShouldWorkOnHalfX(self):
        myT = T.TCurve(self.nominalN)
        self.assertAlmostEquals(myT.gamma(5.0 / 2.0), 1.329, 3)
        
# 300 calculateConstant
# Analysis
#     inputs
#        n -> numeric  mandatory validated
#    outputs
#        float .GE. 0 
#
#     Happy path
#        n:    nominal case     n=5
#     Sad path
#        none ... will prevalidate

    def test300_010_ShouldCalculateLHP(self):
        myT = T.TCurve(self.nominalN)
        self.assertAlmostEquals(myT.calculateConstant(5), 0.37960669, 4)
        
# 400 f
# Analysis
#    inputs
#        n -> numeric mandatory validated
#        u -> float mandatory validated
#    outputs
#        float .GE. 0
# Happy path
#    nominal case:  f(1) -> 0.5787
# Sad path
#            none ... x is pre-validated

    def test400_010_ShouldCalculateFStarterCase(self):
        myT = T.TCurve(self.nominalN)
        self.assertAlmostEquals(myT.f(0, 5), 1, 4)
        
    def test400_020_ShouldCalculateF(self):
        myT = T.TCurve(self.nominalN)
        self.assertAlmostEquals(myT.f(1, 5), 0.578703704)
        
   
   
   
   
   
   
   
   
   
   
   
        
#500(s) integrate
#    Desired level of confidence:    boundary value analysis
#    Input-output Analysis
#                inputs: n    ->     Validated by __init__       Note: Degrees of Freedom (aka Fahrenheit)
#                lowBound     ->
#                highBound    ->.
#       

        #t must be a float, assured by prev function
        #n = 2-30 assured by prev function
#
#        self.nominalN  = 4
#        self.nominalT = 1.4398
#
 #   def integrate(self, t, n, f):
#
# 501 integrates f2() = u**2
# Each of the below tests were precalulated by hand following the Simpson rule

    def test501_001IntegrationOnF2(self):
        myT = T.TCurve(self.nominalN)
        t = 1.0
        n = 1234    #n doesnt matter for f2
        integratedVal = 0.3333333
        self.assertAlmostEquals(myT.integrate(t,n,myT.f2), integratedVal, 3)


    def test501_002IntegrationOnF2(self):
        myT = T.TCurve(self.nominalN)
        t = 4.0
        n = 1234    #n doesnt matter for f2
        integratedVal = 21.3333333
        self.assertAlmostEquals(myT.integrate(t,n,myT.f2), integratedVal, 3)
    
    def test501_003IntegrationOnF2(self):
        myT = T.TCurve(self.nominalN)
        t = 16.0
        n = 1234    #n doesnt matter for f2
        integratedVal = 1365.3333333
        self.assertAlmostEquals(myT.integrate(t,n,myT.f2), integratedVal, 3)




    def test500_901_ShouldRaiseExceptionOnT(self):
        expectedString = "TCurve.integrate:"
        with self.assertRaises(ValueError) as context:
            myT = T.TCurve(23)
            t = 0.0
            n = 1234
            myT.integrate(t,n,myT.f)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])        
        

    # Calc by hnd -> worst idea possible. New rulw is to assum taht above test cases are accurate and work backwords
    def test500_001TDD(self):
        myT = T.TCurve(self.nominalN)
        t = 1.0
        n = 1234    #n doesnt matter yet
        integratedVal = 0.85555275
        self.assertAlmostEquals(myT.integrate(t,n,myT.f), integratedVal,3)
    
    #Test from t dist table corner, working backwards
        # 2 tails
    def test500_010TDD(self):
      
        t = 0.2767
        n = 3
        myT = T.TCurve(n)
        
        # P(a/2)  = .2 
        integratedVal = 0.2 / (myT.calculateConstant(n) * 2)
        self.assertAlmostEquals(myT.integrate(t,n,myT.f), integratedVal, 3)
    

    #Test from t dist table corner, working backwards
        # 1 tail
    def test500_020TDD(self): 
        t = 0.2767
        n = 3
        myT = T.TCurve(n)
        
        # P(a)  = .6 
        testVal = (0.6 - 0.5) / (myT.calculateConstant(n))
        integratedValue = myT.integrate(t,n,myT.f)
        print ("___________   " + str(myT.calculateConstant(n) * integratedValue + .5))
        self.assertAlmostEquals(myT.integrate(t,n,myT.f), testVal, 3)
    








#"Real f function testing" - already know value back tracking to find error
    def test500_101IntegrationOnF(self):
        myT = T.TCurve(self.nominalN)
        t = 1.8946
        n = 7    
        integratedVal = 1.1694779
        self.assertAlmostEquals(myT.integrate(t,n,myT.f), integratedVal, 3)
        #return 1.169477940942020

#    def test502_001IntegrationOnF3(self):
##        myT = T.TCurve(self.nominalN)
 #       t = 1.0
 #       n = 1234    #n doesnt matter for f2
 #       integratedVal = (1.0/7.0)
 #       self.assertAlmostEquals(myT.integrate(t,n,myT.f3, integratedVal)


#    def test502_002IntegrationOnF3(self):
#        myT = T.TCurve(self.nominalN)
#        t = 4.0
#        n = 1234    #n doesnt matter for f2
#        integratedVal = 2340.6
#        self.assertAlmostEquals(myT.integrate(t,n,myT.f3), integratedVal)
    
#Traceback (most recent call last):
#  File "C:\Users\Alex\git\SoftwareProcess\SoftwareProcess\Navigation\test\TCurveTest.py", line 116, in test502_002IntegrationOnF3
#    self.assertAlmostEquals(myT.integrate(t,n,myT.f3), integratedVal)
#AssertionError: 2340.571431114532 != 2340.6 within 7 places
    
