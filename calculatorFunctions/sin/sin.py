__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ['Team A']
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Zbigniew Angelus"
__email__ = "zbigniew.angeluskrzyzanowski@mail.concordia.ca"
__status__ = "Release v1.0"

import sys
from enum import Enum

PI 				= 3.141592653589793
DEGREE 			= PI/180
OUTOFRANGE 		= 'Out of range'

class Angle(Enum):
    DEG=0
    RAD=1
	
def degreeToRadian(angle):
    result = angle*DEGREE
    return result

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
		
def numToPowerOf(base, exponent): 
    if (exponent == 0):
        return 1
    else:
        return base * numToPowerOf(base, exponent - 1);
		
def formatOutput(num):
    numStr = "{0:.7f}".format(num)
    if(numStr=='-0.0000000'):
        return '0'
    elif(numStr=='0.0000000'):
        return '0'
    elif(numStr=='-1.0000000'):
          return '1'
    elif(numStr=='1.0000000'):
          return '1'
    else:
        return numStr
	
def sin(num,Angle = Angle.RAD):
    if(Angle==Angle.DEG):
	    num = degreeToRadian(num)
    if(num<10000000000 and num>-10000000000):
        isMirror=0
        if (num<0):
            isMirror=1
            num=-1*num
        if(num>PI):
            num = num%PI
        result=0
        for n in range(0,10,1):
            result = result + numToPowerOf(-1,n)*(numToPowerOf(num,(2*n+1)))/factorial(2*n+1)
        if (isMirror==1):
            result=-1*result
        return formatOutput(result)
    else:
        return OUTOFRANGE
	
def main():
    pass

if __name__ == "__main__":
    main()
else:
    pass

print(sin(3,0))