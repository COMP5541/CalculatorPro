__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ['Team A']
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Zbigniew Angelus"
__email__ = "zbigniew.angeluskrzyzanowski@mail.concordia.ca"
__status__ = "Unit Test for release 1.0 of the Sin function"

#Unit Test of the Sin function.

import sys
from sin import *

DATA1   		= [[0,0],[-PI/2,-1],[PI/2,1],[-PI,0],[PI,0],[2*PI,0],[-2*PI,0],[-3*PI,0],[3*PI,0]]
DATA2			= [[10000000000,0],[-10000000000,0],[99999999,0.8091447],[-99999999,-0.8091447]]
DEGREESDATA1 	= [[0,0],[45,0.7071068],[90,1],[135,0.7071068],[180,0]]


def getData():
    data = DATA
    return data
	
def testUseCases():
    printReport(DATA1,Angle.RAD,'Unit Test 1 - Sin(x) using radians')
    printReport(DATA2,Angle.RAD, 'Unit Test 2 - Sin(x) limits using radians')
    printReport(DEGREESDATA1,Angle.DEG, 'Unit Test 3 - Sin(x) using degrees')

def printReport(data, Angle,uc):
    failed=0
    for i in range(len(data)):
        datax,datay = data[i]
        calculation = sin(datax,Angle)
        if(calculation == OUTOFRANGE):
            print("Passed: Sin({0}) is {1} as expected".format(datax, OUTOFRANGE))
        else:
            data2String = formatOutput(datay)
            if(calculation!=data2String):
                print("Error: Sin({0}) should be {1} but the result is {2}".format(datax, data2String,calculation))
                failed +=1
            else:
                print("Passed: Sin({0}) is {1}".format(datax,calculation)) 
    if (failed==0):
        print('---------------------------')
        print("SUMMARY: {0} - Results as expected".format(uc))
        print('---------------------------')
	
	
def main():
    testUseCases()

if __name__ == "__main__":
    main()
else:
    pass