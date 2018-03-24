

#OUTPUT
def calc_output(x):
    return round(x,6)


#Approximation of PI
PI = 3.141592653589793

DEGREE 			= PI/180
OUTOFRANGE 		= 'Out of range'

#Variable for 10exp function
LN_10 = 2.30258509299405

# Factorial: n!
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


#Approximation of Euler's constant, E = 2.718281828459045
def e():
    n = 17
    sum1 = 1
    for i in range(1, n + 1):
        sum1 = sum1 + (1 / factorial(i))
    return sum1
    #print("The sum of series is", sum1)

#Constant
E = e()

# Absolute:|n|
def myAbs(n):
    if (n<0):
        return -n
    else:
        return n

'''
# Exponent: base to the power exp (base^exp)
def power(base, exp):
    if isinstance(base, (int, float)) and isinstance(exp, int):

        if base == 0:
            return 0

        if exp == 0:
            return 1

        if (exp == 1):
            return (base)

        # Positive Values
        if exp > 0:
            return base * power(base, exp - 1)

        # Negative Values
        elif exp < 0:
            return 1 / float(power(base, -exp))
    else:
        print('X must be a number and Y must be an integer')
'''

#Exponent for integers
def power(a,b):

    #Handle exceptions
    if (b==0):
        return 1

    #Initialize vairiables
    i = 1
    r = a

    if (b>0):
        while (i<b):
            #print(a)
            r*=a
            i+=1

        return r
    else:
        b=-b
        while (i<b):
            r*=a
            i+=1
        return 1/r


print(power(2,-1))