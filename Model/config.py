
#Approximation of PI
PI = 3.141592653589793


#Variable for 10exp function
LN_10 = 2.30258509299405


#FOR SIN(X) FUNCTION
DEGREE 			= PI/180
OUTOFRANGE 		= 'Out of range'


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

#Euler's Constant
E = e()

# Absolute:|n|
def myAbs(n):
    if (n<0):
        return -n
    else:
        return n

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


#print(power(2,-1))