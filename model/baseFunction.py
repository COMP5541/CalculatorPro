__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ['Team A']
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Team A"
__email__ = "TeamA@mail.concordia.ca"
__status__ = "Release v1.0"

import sys
from enum import Enum
import decimal

from abc import ABC
from abc import abstractmethod

OUTOFRANGE = 'Out of range'

class CommonToFunction(ABC):

    out_of_range_message = OUTOFRANGE

    #@abstractmethod
    def formatOutput(self,num):
        numStr = "{0:.7f}".format(num)
        if (numStr == '-0.0000000'):
            return '0'
        elif (numStr == '0.0000000'):
            return '0'
        elif (numStr == '-1.0000000'):
            return '1'
        elif (numStr == '1.0000000'):
            return '1'
        else:
            return numStr
            # TODO -- use own power function implmentation

    # ToDo -- use own power function implmentation
    def arctan(self,x):
        d = decimal.Decimal
        with decimal.localcontext() as context:
            context.prec += 4
            result = d(0)
            for n in range(0, 20, 1):
                result = result + ((d(-1)) ** n) * (x ** (d(2) * n + d(1))) / (d(2) * n + d(1))
        return result

    def piconstant(self):
        d = decimal.Decimal
        return d(4) * (d(4) * self.arctan(d(1 / 5)) - self.arctan(d(1 / 239)))