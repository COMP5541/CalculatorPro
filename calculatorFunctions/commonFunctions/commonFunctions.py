__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Beranrdo Sandi"
__email__ = "B_SANDI@encs.concordia.ca"
__status__ = "Release v1.0"


# Exponent: base to the power exp (base^exp)
def power(base, exp):
    if isinstance(base, (int, float)) and isinstance(exp, int):

        if base==0:
          return 0

        if exp==0:
            return 1

        if (exp == 1):
            return (base)

        # Positive Values
        if exp >0:
            return base * power(base, exp - 1)

        # Negative Values
        elif exp < 0:
            return 1/float(power(base, -exp))
    else:
        print ('X must be a number and Y must be an integer')



# Factorial: n!
def factorial(n):
    if n == 1:
        return n
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Factorial: n!
def my_abs(n):
    if (n==0):
        return 0
    if (n<0):
        return -n
    else:
        return n