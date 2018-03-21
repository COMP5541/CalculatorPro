__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ['Team A']
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Team A"
__email__ = "TeamA@mail.concordia.ca"
__status__ = "Release v1.0"

import math
import decimal

def econstant():
    n = 17
    sum1 = 1
    for i in range(1, n + 1):
        sum1 = sum1 + (1 / math.factorial(i))
    return sum1

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

# ToDo -- use own power function implmentation
def arctan(x):
    d = decimal.Decimal
    with decimal.localcontext() as context:
        context.prec += 4
        result = d(0)
        for n in range(0, 20, 1):
            result = result + ((d(-1)) ** n) * (x ** (d(2) * n + d(1))) / (d(2) * n + d(1))
    return result

def piconstant():
    d = decimal.Decimal
    return d(4) * (d(4) * arctan(d(1 / 5)) - arctan(d(1 / 239)))


def e():
    n = 17
    sum1 = 1
    for i in range(1, n + 1):
        sum1 = sum1 + (1 / math.factorial(i))
    return sum1
    #print("The sum of series is", sum1)

