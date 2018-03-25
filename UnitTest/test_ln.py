from Model.config import *
from Model.log import *
import math

def test_ln():
    max = 10 ** 10
    min = -max
    small = 10 ** (-10)

    print("Test ln(x):")
    print(ln(max))
    print(ln(min))
    print(ln(small))

    print(math.log(max))
    #print(math.log(min))
    print(math.log(small))

#TEST
if __name__ == "__main__":
    test_ln()