from Model.config import *
from Model.sin import *
import math

#Define test functions
def test(x):
    print("ETERNITY result for " + str(x))
    result = sin(x)
    print(result)

def benchmark(x):
    print("math library result for " + str(x))
    result = math.sin(x)
    print(result)

def run_test():

    input_values = [test_max, test_min, test_small, 0, 1]

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
