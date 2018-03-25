__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ['Team A']
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Team A"
__email__ = "TeamA@mail.concordia.ca"
__status__ = "Release v1.0"

#Import utilities
import decimal

#VALUE_ERROR
VALUE_ERROR = "Value Error"

#Range variables for testing
test_max = 10 ** 10
test_min = -test_max
test_small = 10 ** (-10)

#Variable for 10exp function
LN_10 = 2.30258509299405

# Factorial: n!
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

#Approximation of Euler's constant, E = 2.718281828459045
def e():
    n = 17
    sum1 = 1
    for i in range(1, n + 1):
        sum1 = sum1 + (1 / factorial(i))
    return sum1
    #print("The sum of series is", sum1)

#Euler's Constant
E = e()

# Absolute:|n|
def myAbs(n):
    if (n<0):
        return -n
    else:
        return n

#Exponent for integers
def power(a,b):

    #Handle exceptions
    if (b==0):
        return 1

    #Initialize vairiables
    i = 1
    r = a

    if (b>0):
        while (i<b):
            #print(a)
            r*=a
            i+=1

        return r
    else:
        b=-b
        while (i<b):
            r*=a
            i+=1
        return 1/r

# ToDo -- use own power function implementation
def arctan(x):
    d = decimal.Decimal
    with decimal.localcontext() as context:
        context.prec += 4
        result = d(0)
        for n in range(0, 20, 1):
            result = result + ((d(-1)) ** n) * (x ** (d(2) * n + d(1))) / (d(2) * n + d(1))
    return result

def piconstant():
    d = decimal.Decimal
    return d(4) * (d(4) * arctan(d(1 / 5)) - arctan(d(1 / 239)))

#Approximation of PI
#PI = 3.141592653589793
PI = piconstant()

#FOR SIN(X) FUNCTION
DEGREE 			= PI/180
OUTOFRANGE 		= 'Out of range'