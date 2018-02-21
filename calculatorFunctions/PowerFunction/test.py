__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Faezeh Mobasheri"
__email__ = "f_mobas@encs.concordia.ca"
__status__ = "Release v1.0"


from calculatorFunctions.PowerFunction.tentopowerx import tentopower
import math

#Calculation Test1
test1 = 2.2
print("test case 1:")
print("If x is floating number and positive calculated result is:")
print(tentopower(test1))
print("If x is floating number and positive returned result form pyhton is:")
print(10**test1)

#Calculation Test2
print("\n")
print("test case 2")
test2= -6.8
print("If x is floating number and negative calculated result is:")
print(tentopower(test2))
print("If x is floating number and negative returned result form pyhton is:")
print(10**test2)

#power function test
print("\n")
print("test case 3")
print("If x is an integer and positive number calculated result is:")
print(tentopower(3))
print("If x is an integer and positive number returned result from Python is:")
print(math.pow(10, 3))


#factorial function test
print("\n")
print("test case 4")
print("If x is an integer and negative number calculated result is:")
print(tentopower(-6))
print("If x is an integer and positive number returned result from Python is:")
print(math.pow(10, -6))



