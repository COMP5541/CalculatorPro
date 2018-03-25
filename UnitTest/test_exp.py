from Model.config import *
from Model.exp import *
import math

#Define test functions
def test(x):
    print("ETERNITY result for " + str(x))
    result = exp(x)
    print(result)

def benchmark(x):
    print("math library result for " + str(x))
    result = math.exp(x)
    print(result)

def run_test():

    input_values = [100, -100, test_small, 0, 1]

    for x in input_values:
        test(x)

    for x in input_values:
        try:
            benchmark(x)
        except ValueError:
            print("ValueError")

# TEST
if __name__ == "__main__":
    run_test()