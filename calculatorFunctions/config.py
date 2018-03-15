import math


#Error variables
error = 0.000001
error_decimals = 6

#Approximation of natural number e
E = 2.718281828459045

#Approximation of PI
PI = 3.141592653589793

DEGREE 			= PI/180
OUTOFRANGE 		= 'Out of range'


'''
#Approximation of natural number e
def e():
    n = 17
    sum1 = 1
    for i in range(1, n + 1):
        sum1 = sum1 + (1 / math.factorial(i))
    print("The sum of series is", sum1)
'''

# Factorial: n!
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Absolute:|n|
def my_abs(n):
    if (n<0):
        return -n
    else:
        return n

# Exponent: base to the power exp (base^exp)
def power(base, exp):
    if isinstance(base, (int, float)) and isinstance(exp, int):

        if base == 0:
            return 0

        if exp == 0:
            return 1

        if (exp == 1):
            return (base)

        # Positive Values
        if exp > 0:
            return base * power(base, exp - 1)

        # Negative Values
        elif exp < 0:
            return 1 / float(power(base, -exp))
    else:
        print('X must be a number and Y must be an integer')
