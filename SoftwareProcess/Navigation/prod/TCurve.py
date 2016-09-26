import math
class TCurve(object):

# outward facing methods
    def __init__(self, n=None):
        functionName = "TCurve.__init__: "
        if(n == None):
            raise ValueError(functionName + "invalid n")
        if(not(isinstance(n, int))):
            raise ValueError(functionName + "invalid n")
        if((n < 2) or (n >= 30)):
            raise ValueError(functionName + "invalid n")
        self.n = n

    
    def p(self, t=None, tails=1):
        functionName = "TCurve.p: "
        if(t == None):
            raise ValueError(functionName + "missing t")
        if(not(isinstance(t, float))):
            raise ValueError(functionName + "invalid t")
        if(t < 0.0):
            raise ValueError(functionName + "invalid t")
        
        if(not(isinstance(tails, int))):
            raise ValueError(functionName + "invalid tails")
        if((tails != 1) & (tails != 2)):
            raise ValueError(functionName + "invalid tails")
        
        constant = self. calculateConstant(self.n)
        integration = self.integrate(t, self.n, self.f)
        if(tails == 1):
            result = constant * integration + 0.5
        else:
            result = constant * integration * 2
            
        if(result > 1.0):
            raise ValueError(functionName + "result > 1.0")
        
        return result
        
# internal methods
    def gamma(self, x):
        if(x == 1):
            return 1
        if(x == 0.5):
            return math.sqrt(math.pi)
        return (x - 1) * self.gamma(x - 1)
    
    def calculateConstant(self, n):
        n = float(n)
        numerator = self.gamma((n + 1.0) / 2.0)
        denominator = self.gamma(n / 2.0) * math.sqrt(n * math.pi)
        result = numerator / denominator
        return result
    
    def f(self, u, n):
        n = float(n)
        base = (1 + (u ** 2) / n)
        exponent = -(n + 1.0) / 2
        result = base ** exponent
        return result
        
    def f2(self, u, n):
        return u**2
    
    def f3(self, u, n):
        return u**6
       
    
    def integrate(self, t, n, f):
        epsilon = 0.000001         #Assert requires 7 degrees of certainity
        simpsonOld = 0
        simpsonNew = epsilon
        s = 4.0
        
        inplace = 0
        consant = 0
        w = 0
        
        num = simpsonNew - simpsonOld
        den = simpsonNew
        
        #  without separating kept throwing div by 0 errors
        if(den == 0):
            raise ValueError("TCurve.integrate: invalid t")  
        if(num < 0):
            num = abs(num)
        while((num/den) > epsilon):
            highBound = t
            lowBound = 0
            
            simpsonOld = simpsonNew
            w = (highBound - lowBound)/s
            constant = (w/3.0)
            
            inplace = 0
            init = 2
            tini = 2
            
            inplace = 1 * f(lowBound,n)
            
            while(lowBound < highBound):    
                #just a simple 2 or 4 result for init.  Leaves at 4 to start,
                init = init + tini
                tini *= -1
                
                inplace += (init * f(lowBound,n))
            
              
                                
                lowBound = lowBound + w
            ##NEED highBound to be times 1 (this is the missing s+1 value)
            inplace += (1 * f(highBound,n))
   
            simpsonNew = inplace * constant        
            
     #       print(str(simpsonNew) + "  "+ str(inplace) + "  " + str(constant))
            
            num = simpsonNew - simpsonOld
            den = simpsonNew
        
            # Not going to test, but without seperating kept throwing div by 0 errors
            if(den == 0):
                raise ValueError("TCurve.integrate: invalid t")  
            if(num < 0):
                num = abs(num)

            s = s*2

        return simpsonNew
        
        
