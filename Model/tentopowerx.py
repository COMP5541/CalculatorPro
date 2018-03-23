__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Faezeh Mobasheri"
__email__ = "f_mobas@encs.concordia.ca"
__status__ = "Release v1.0"

from Model.config import LN_10
from Model.config import factorial
from Model.config import myAbs
from Model.config import power


#Exponent for real numbers
def exp10(x):

    if x ==0:
        return 1
    if x ==1:
        return 10

    #Check for decimals
    decimals = myAbs(x - int(x))
    #print("integer: " + str(int(e)))
    #print("decimals: " + str(decimals))

    #Compute exponent
    if decimals == 0:
        return power(10, int(x))

    if decimals > 0:
        sum = 1
        for k in range(1,10):
            sum+=power(decimals*LN_10,k)*1/factorial(k)

        if x > 0:
            return power(10,int(x))*sum
        if x < 0:
            return 1/(power(10,myAbs(int(x)))*sum)

'''
def tentopower(x):
    A=loge(10)
    B=x*A
    result=exp.fun_ex(B)
    return result


'''

#print(tentopower(24.9))
#print(pow(10, 24.9))