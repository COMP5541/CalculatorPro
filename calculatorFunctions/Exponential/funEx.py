
#Created on Feb 18, 2018
#Function to calculate value  raise to the power x using Taylor Series
#@author: ratol


# for positive numbers range is up-to 40
# for negative numbers range is up-to -15

def fun_ex(value):
    thesum = 1.0
    for i in range(100, 0, -1):
        thesum = 1 + value * thesum / i
    return thesum
