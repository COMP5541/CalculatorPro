__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Faezeh Mobasheri"
__email__ = "f_mobas@encs.concordia.ca"
__status__ = "Release v1.0"

from Model import exp

from Model.ln import loge


def tentopower(x):
    A=loge(10)
    B=x*A
    result=exp.fun_ex(B)
    return result

#print(tentopower(24.9))
#print(pow(10, 24.9))