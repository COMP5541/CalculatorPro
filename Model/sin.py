__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ['Team A']
__license__ = "GPL"
__version__ = "1.1"
__maintainer__ = "Zbigniew Angelus"
__email__ = "zbigniew.angeluskrzyzanowski@mail.concordia.ca"
__status__ = "Release v1.0"

#Import utilities

from Model.config import factorial
from Model.config import PI as pi
from Model.config import power
from Model.config import degreeToRadian
import math


def sin(num):
    isMirror = 0
    if (num < 0):
        isMirror = 1
        num = -1 * num
    negativeRange=0
    if (num> pi):
        quotien= num//pi
        num = num % pi
        if quotien % 2 == 0:
            negativeRange = 0  # Even
        else:
            negativeRange = 1  # Odd
    result = 0
    for n in range(0, 10, 1):
        result = result + power(-1, n) * (power(num, (2 * n + 1))) / factorial(2 * n + 1)
    if(negativeRange ==1):
        result = -1 * result
    if (isMirror == 1 ):
        result = -1 * result
    return result

def main():
    pass

def ut1():
    list1 = [-1.4, -2.4, -3.4, -4.4, -5.4, -6.4, -7.4, -8.4, -9.4, 1.4, 2.4, 3.4, 4.4, 5.4, 6.4, 7.4, 8.4,9.4]
    for x in list1:
        epsilon = 0.000000001
        result = abs(math.sin(x) - sin(x))
        if result > epsilon:
            print(str(x) + ' has discrepancy ' + str(result))
        else:
            print('Test sin(' + str(x) + ')' + ' passed')

def ut2():
    list2 = [30, 60, 90, 180, 45, -30, -60, -90, -180, -45]
    for x in list2:
        epsilon = 0.000000001
        result = abs(math.sin(math.radians(x)) - sin(degreeToRadian(x)))
        if result > epsilon:
           print(str(x) + ' has discrepancy ' + str(result) )
        else:
           print('Test sin('+str(x)+')'+' passed')#

if __name__ == "__main__":
    ut1()
    ut2()
else:
    pass
