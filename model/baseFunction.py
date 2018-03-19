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
import model.baseLibrary as lib
from model.baseLibrary import *

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

    def piconstant(self):
        return lib.piconstant()

    def econstant(self):
        return lib.e()