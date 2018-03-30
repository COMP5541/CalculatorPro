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

def sin(num,type):
    isMirror = 0
    if (num < 0):
        isMirror = 1
        num = -1 * num

    if type == True:
        cut = pi
    else:
        cut = 180

    negativeRange=0
    if (num> cut):
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

if __name__ == "__main__":
    main()
else:
    pass
