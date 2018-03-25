from Model.config import *
from Model.log import *
import math

#Define test functions
def test(x):
    print("ETERNITY Test for " + str(x))
    print(str(ln(x)))

def run_test():

    test(test_max)
    test(test_min)
    test(test_small)
    test(0)
    test(1)

#TEST
if __name__ == "__main__":
    run_test()