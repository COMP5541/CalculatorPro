__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Jasdeep Ratol"
__email__ = " j_ratol@encs.concordia.ca"
__status__ = "Release v1.0"





import math

from calculatorFunctions.Exponential.funEx import fun_ex

# Test 1 (value = positive integer)
if fun_ex(5) == math.exp(5):
    print('Passed for positive input')


# Test 2 (value =  negative integer)

if fun_ex(-5) == math.exp(-5):
    print('Passed for negative input')
else:
    print("Some error for negative input")

# Test 3 (value = zero)
if fun_ex(0) == math.exp(0):
    print(' Passed for input Zero')
