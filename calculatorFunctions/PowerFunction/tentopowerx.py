__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Faezeh Mobasheri"
__email__ = "f_mobas@encs.concordia.ca"
__status__ = "Release v1.0"

import math

value = 1
ln10 = math.log(10)

#Define precision decimal
error=0.000000000001
error_decimal=10


#Calculation of power function
def power(base,exp):
    if (exp==0):
        return 1
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))


#calculation of factorial function
def factorial(n):
        if n == 1:
            return n
        if n==0:
            return 1
        else:
            return n * factorial(n - 1)


#if the value of X is an integer use power function, if it is floating number taylor series formula
def tentopower(x):
    val=x
    if type(val)==int:
            if val >= 0 :
               return (power(10, val))
            if val < 0 :
               val *= -1
            return (1/power(10, val))
    elif type(val)==float:
        if val>=0:
            value = 0.0000000000000000000001
            for n in range(150):
                calculate = ((power(ln10, n)) * (power(val + 22, n)) * 0.0000000000000000000001) / factorial(n)
                if calculate > error:
                  value += calculate
                else:
                  value += 0
                  round(calculate, error_decimal)
            return (value)
        if val<0:
            val *= -1
            value = 0.0000000000000000000001
            for n in range(150):
                calculate = ((power(ln10, n)) * (power(val + 22, n)) * 0.0000000000000000000001) / factorial(n)
                if calculate > error:
                  value += calculate
                else:
                  value += 0
                  round(calculate, error_decimal)
            return (1/value)

