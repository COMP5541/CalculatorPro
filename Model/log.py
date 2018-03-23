__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Agustin Gimenez Comas"
__email__ = "a_gimene@encs.concordia.ca"
__status__ = "Release v1.0"




from Model.config import E
from Model.config import error
from Model.config import error_decimals
from Model.config import myAbs
from Model.exp import exp

'''
Algorithm for ln(x) using Binary Search
Properties of the natural logarithm
If x < 1: a useful property is ln(1/x)=-ln(x)
If x > e: a useful property is ln(x/e) = ln(x)-ln(e) --> ln(x)=ln(x/e)+1


#Natural Logarithm
def loge(x):
    #Handle exceptional cases
    if (x==1):
        return 0
    if (x==0):
        return float('-Inf')
    if (x<0):
        return float('nan')
    
    #Use recursion to get approximative range
    if(x<1):
        return (-loge(1.0/x))
    if(x>E):
        return (loge(x/E)+1.0)
    
    #Binary Search Approach
    lo=0.0
    hi=1.0

    while(True):
        mid=(lo+hi)/2.0
        val= exp(mid) #Python exponent operator
        if (val>x):
            hi=mid
        if(val<x):
            lo=mid
        if (myAbs(val-x)<error):
            return mid

'''


'''
Algorithm for computing the base-10 logarithm based on the
Mathematical-Function Computation Handbook [Beebe]
'''

#Base-10 Logarithm
def log10(x):
    # Handle exceptional cases
    if (x == 1):
        return 0
    if (x == 0):
        return float('-Inf')
    if (x < 0):
        return float('nan')

    n = 0 #Start exponent of base 10

    #Normalize input
    while (x >= 1.0):
        x = x/10.0
        n+=1

    # if x <= sqrt(1/10)
    while(x<=0.316227766016838):
        x = x*10.0
        n = n-1

    #Produce a change of variable
    z = (x-1.0)/(x+1.0)
    D = 0.868588964 #2*log10(e)

    #Taylor series approximation
    sum = z
    for k in range(3,23,2):
        sum+=(z**k)/k #used ** instead of my_exp() for simplicity

    return D*sum+n,6


def ln(x):
    return (log10(x)/log10(E))


if __name__ == "__main__":            
    test=5 #Enter whatever input you want to test
    print(loge(test))
    print(math.log(test))   
