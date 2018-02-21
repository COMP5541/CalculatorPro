import math

from calculatorFunctions.Exponential.funEx import fun_ex

# Test 1 (value = positive integer)
if fun_ex(5) == math.exp(5):
    print('passed for positive integer')


# Test 2 (value =  negative integer)

if fun_ex(-5) == math.exp(-5):
    print('passed for negative value')
else:
    print("Some error for negative value")

# Test 3 (value = zero)
if fun_ex(0) == math.exp(0):
    print('passed for Zero')
