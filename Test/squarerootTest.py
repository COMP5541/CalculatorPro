__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Beranrdo Sandi"
__email__ = "B_SANDI@encs.concordia.ca"
__status__ = "Release v1.0"

from random import random
from calculatorFunctions.squareroot import squareroot

error = 0.0000000001

# Test positive numbers and 0
def testPositive ():
    n = 0
    for i in range(1000):
        num = random()*100000
        if calculatorFunctions.my_abs(squareroot.squareroot(num) * squareroot.squareroot(num) - num)  <= error :
            n += 1
            pass
        else:
            return print("Error found")

    return print("Test for positive numbers passed. Number of test executed " + str(n))


# Test negative numbers
def testNegative ():
    pass


# Report of test executed
def testReport ():
    testPositive()
    testNegative()
testReport()