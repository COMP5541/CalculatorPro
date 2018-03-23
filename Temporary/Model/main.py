__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ['Team A']
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Team A"
__email__ = "TeamA@mail.concordia.ca"
__status__ = "Release v1.0"

import Temporary.Model.baseLibrary as lib
import decimal
from Temporary.Model.baseLibrary import *

d = decimal.Decimal
pi = lib.piconstant()
E = lib.econstant()
degree = pi / d(180)

#Error variables
error = 0.000001
error_decimals = 6

def degreeToRadian(angle):
    angle = d(angle)
    return degree * angle

def numToPowerOf(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * numToPowerOf(base, exponent - 1)

def sin(num):
    #num = d(num)
    radian = True
    #if (radian == False):
    #    num = degreeToRadian(num)
    isMirror = 0
    if (num < 0):
        isMirror = 1
        num = -1 * num
    if (num > pi):
        num = num % pi
    result = 0
    for n in range(0, 10, 1):
        a = numToPowerOf(-1, n)
        b = (numToPowerOf(num, (2 * n + 1)))
        c = factorial(2 * n + 1)
        result = result + a*b/c
        #result = result + numToPowerOf(-1, n) * (numToPowerOf(num, (2 * n + 1))) / factorial(2 * n + 1)
    if (isMirror == 1):
        result = -1 * result
    return result

def squareroot(num):
    #To be implemented here
    return 11

def funEx(num):
    # To be implemented here
    return 12

def ln(num):
    # To be implemented here
    return 13

def tentopower(num):
    # To be implemented here
    return 14

#def loge(num):
#    # To be implemented here
#    return 15


def loge(x):
    # Handle exceptional cases
    if (x == 1):
        return 0
    if (x == 0):
        return float('-Inf')
    if (x < 0):
        return float('nan')

    # Use recursion to get approximative range
    '''
    Properties of the natural logarithm
    If x < 1: a useful property is ln(1/x)=-ln(x)
    If x > e: a useful property is ln(x/e) = ln(x)-ln(e) --> ln(x)=ln(x/e)+1
    '''
    if (x < 1):
        return (-loge(1.0 / x))
    if (x > E):
        return (loge(x / E) + 1.0)

    # Binary Search Approach
    lo = 0.0
    hi = 1.0

    while (True):
        mid = (lo + hi) / 2.0
        val = E ** mid  # Python exponent operator
        if (val > x):
            hi = mid
        if (val < x):
            lo = mid
        if (my_abs(val - x) < error):
            return round(mid, error_decimals)

def fun_ex(num):
    # To be implemented here
    return 16