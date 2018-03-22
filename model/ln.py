__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Agustin Gimenez Comas"
__email__ = "a_gimene@encs.concordia.ca"
__status__ = "Release v1.0"

'''
Properties of the natural logarithm
If x < 1: a useful property is ln(1/x)=-ln(x)
If x > e: a useful property is ln(x/e) = ln(x)-ln(e) --> ln(x)=ln(x/e)+1

'''



#Import math until other functions available
import math
# Import math until other functions available
import math

from model.config import e
from model.config import error
from model.config import error_decimals
from model.config import myAbs

#Value of Euler's constant
E = e()

def loge(x):
    #Handle exceptional cases
    if (x==1):
        return 0
    if (x==0):
        return float('-Inf')
    if (x<0):
        return float('nan')
    
    #Use recursion to get approximative range
    '''
    Properties of the natural logarithm
    If x < 1: a useful property is ln(1/x)=-ln(x)
    If x > e: a useful property is ln(x/e) = ln(x)-ln(e) --> ln(x)=ln(x/e)+1
    '''
    if(x<1):
        return (-loge(1.0/x))
    if(x>E):
        return (loge(x/E)+1.0)
    
    #Binary Search Approach
    lo=0.0
    hi=1.0

    while(True):
        mid=(lo+hi)/2.0
        val= E ** mid #Python exponent operator
        if (val>x):
            hi=mid
        if(val<x):
            lo=mid
        if (myAbs(val-x)<error):
            return round(mid,error_decimals)

if __name__ == "__main__":            
    test=5 #Enter whatever input you want to test
    print(loge(test))
    print(math.log(test))   
