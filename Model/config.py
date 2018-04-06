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

#Range variables for testing
test_max = 10 ** 10
test_min = -test_max
test_small = 10 ** (-10)

#Variable for 10exp function
LN_10 = 2.30258509299405

def arctan(x):
    result = 0
    for n in range(0, 20, 1):
        result = result + ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
    return result

#PI CONSTANT
def piconstant():
    return 4 * (4 * arctan(1 / 5) - arctan(1 / 239))

PI = piconstant()

#DEGREE FOR SIN(X)
def degreeToRadian(angle):
    angle = angle
    return DEGREE * angle

DEGREE = piconstant()/180


#OUTOFRANGE 		= 'Out of range'


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

