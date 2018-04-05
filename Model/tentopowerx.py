__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ["Team A"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Faezeh Mobasheri"
__email__ = "f_mobas@encs.concordia.ca"
__status__ = "Release v1.0"



from Model.config import myAbs, power, factorial, LN_10


#power series of 10^x function
def tentopowerx(x):
    if (myAbs(x)>100):
        return "Out of Range"

    if type(x)==int:

        if x==0:
           return 1

        elif x==1:
           return 10

        else:
            return power(10, x)

    elif type(x)==float:

        e=int(x)
        decimal=myAbs(x-e)
        tentopower=0
        n=0
        Ln10=LN_10
        term=((power(decimal*Ln10, n))/(factorial(n)))

        while myAbs(term) > (1 * 10 ** (-14)):
            tentopower += term
            n +=1
            term = (power(decimal * Ln10, n)) / (factorial(n))

        if x>0:
            return power(10, e)*tentopower

        else:
            return 1/(power(10,myAbs(e))*tentopower)
