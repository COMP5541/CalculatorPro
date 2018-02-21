
#Title: 10^x
#Author: Faezeh
#Date: 18 feb
#Team A, COMP 5541 Winter 2018, Concordia University


import math

value = 1
ln10 = math.log(10)

#Define precision decimal
error=0.000000000001


#Calculation of power function
def power(base,exp):
    if (exp==0):
        return 1
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))


#calculation of factorial function
def factorial(n):
        if n == 1:
            return n
        if n==0:
            return 1
        else:
            return n * factorial(n - 1)


#if the value of X is an integer use power function, if it is floating number use tentopower(x) function
def get_value():
    user_input = input()
    try:
        val = int(user_input)
        if val >= 0 :
            print(power(10, val))
        if val <0 :
            val *= -1
            print(1/power(10, val))
    except ValueError:
        val = float(user_input)
        print(tentopower(val))


#Calculation of 10^x when X is floating number
def tentopower(x):
    value= 0.0000000000000000000001
    for n in range(150):
        calculate= ((power (ln10, n))*(power(x+22, n))* 0.0000000000000000000001)/factorial(n)
        if calculate > error:
            value +=calculate
        else :
           value += 0
    return value



#Get value of x from user and return 10^x
print("\n")
print("Caculator is on:")
get_value()


