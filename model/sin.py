__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ['Team A']
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Zbigniew Angelus"
__email__ = "zbigniew.angeluskrzyzanowski@mail.concordia.ca"
__status__ = "Release v1.0"

import decimal
from model.baseLibrary import *
import model.baseLibrary as lib

d = decimal.Decimal
pi = lib.piconstant()
E = lib.econstant()
degree = pi / d(180)

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
	
def main():
    pass

if __name__ == "__main__":
    main()
else:
    pass