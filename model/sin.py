__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ['Team A']
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Team A"
__email__ = "TeamA@mail.concordia.ca"
__status__ = "Release v1.0"

import sys
from enum import Enum
import decimal
from model.baseFunction import CommonToFunction as CTF

class Sin(CTF):
    def __init__(self):
        self.d = decimal.Decimal
        self.pi = super().piconstant()
        # default angle type is radian
        self.radian = True
        self.degree = self.pi / self.d(180)

    def switchAngleType(self, radian):
        # True to set angle to Radian, False to Degrees
        self.radian = radian

    def calculate(self, num):
        num = self.d(num)
        if (self.radian == False):
            num = self.degreeToRadian(num)
        if (num < self.d(10000000000) and num > self.d(-10000000000)):
            isMirror = 0
            if (num < self.d(0)):
                isMirror = 1
                num = self.d(-1) * num
            if (num > self.pi):
                num = num % self.pi
            result = 0
            for n in range(0, 10, 1):
                result = result + self.numToPowerOf(-1, n) * (self.numToPowerOf(num, (2 * n + 1))) / self.factorial(
                    2 * n + 1)
            if (isMirror == 1):
                result = -1 * result
            return result
                    #self.formatOutput(result)
        else:
            return super().out_of_range_message

    def degreeToRadian(self, angle):
        angle = self.d(angle)
        return self.degree * angle

    def factorial(self, n):
        if n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def numToPowerOf(self, base, exponent):
        if (exponent == 0):
            return 1
        else:
            return base * self.numToPowerOf(base, exponent - 1);

def main():
    testSin = Sin()
    print(testSin.calculate(3.14))
    print(testSin.pi)

if __name__ == '__main__':
    main()
