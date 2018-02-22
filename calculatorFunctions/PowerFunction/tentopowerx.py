__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Faezeh Mobasheri"
__email__ = "f_mobas@encs.concordia.ca"
__status__ = "Release v1.0"

import math
#from calculatorFunctions.log.ln import loge
#from calculatorFunctions.Exponential.funEx import fun_ex

def tentopower(x):
    A=math.log(10)
    B=x*A
    result=math.exp(B)
    return result

print(tentopower(100.8))
print(10**100.8)
