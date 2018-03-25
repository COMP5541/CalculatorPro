__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Agustin Gimenez Comas"
__email__ = "a_gimene@encs.concordia.ca"
__status__ = "Release v1.0"


from Model.config import E, VALUE_ERROR
from Model.config import myAbs
from Model.exp import exp

'''
Algorithm for ln(x) using Binary Search
Properties of the natural logarithm
If x < 1: a useful property is ln(1/x)=-ln(x)
If x > e: a useful property is ln(x/e) = ln(x)-ln(e) --> ln(x)=ln(x/e)+1
'''

#Natural Logarithm
def ln(x):
    error = 0.0000000001 #High-enough precision
    #Handle exceptional cases
    if (x==1):
        return 0
    if (x==0):
        return VALUE_ERROR
    if (x<0):
        return VALUE_ERROR
    
    #Use recursion to get approximative range
    if(x<1):
        return (-ln(1.0/x))
    if(x>E):
        return (ln(x/E)+1.0)
    
    #Binary Search Approach
    lo=0.0
    hi=1.0

    while(True):
        mid=(lo+hi)/2.0
        val= exp(mid)
        if (val>x):
            hi=mid
        if(val<x):
            lo=mid
        if (myAbs(val-x)<error):
            return mid


if __name__ == "__main__":            
    pass
