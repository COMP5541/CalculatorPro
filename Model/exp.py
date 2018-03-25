__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Jasdeep Ratol"
__email__ = " j_ratol@encs.concordia.ca"
__status__ = "Release v1.0"

from Model.config import E, factorial, myAbs, power

#Exponent for real numbers for basis e
def exp(x):

    if x==0:
        return 1
    if x ==1:
        return E

    #Check for decimals
    decimals = myAbs(x - int(x))

    #Compute exponent
    if decimals == 0:
        return power(E, int(x))

    if decimals > 0:
        sum = 1     #power series
        n = 1       #initialize n
        term = 1    #power series expansion term

        while myAbs(term) > 10**(-14):
            term = power(decimals,n)/factorial(n)
            sum+=term
            n+=1

        if x > 0:
            return power(E,int(x))*sum
        if x < 0:
            return 1/(power(E,myAbs(int(x)))*sum)

