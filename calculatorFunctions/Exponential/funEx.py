__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Jasdeep Ratol"
__email__ = " j_ratol@encs.concordia.ca"
__status__ = "Release v1.0"


# for positive numbers range is up-to 40
# for negative numbers range is up-to -15

def fun_ex(value):
    thesum = 1.0
    for i in range(100, 0, -1):
        thesum = 1 + value * thesum / i
    return thesum
