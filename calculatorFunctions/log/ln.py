'''
Created on Feb 16, 2018
@author: Gus
Team A, COMP 5541 Winter 2018, Concordia University

Properties of the natural logarithm
If x < 1: a useful property is ln(1/x)=-ln(x)
If x > e: a useful property is ln(x/e) = ln(x)-ln(e) --> ln(x)=ln(x/e)+1

'''
import math

#Define target precision
error=0.0000000001
error_decimals = 10

#Approximation of natural number e
e = 2.718281828459045 

def my_abs(n):
    if (n==0):
        return 0
    if (n<0):
        return -n
    else:
        return n

def loge(x):
    #Handle exceptional cases
    if (x==1):
        return 0
    if (x==0):
        return float('-Inf')
    if (x<0):
        return float('nan')
    
    #Use recursion to get approximative range
    '''
    Properties of the natural logarithm
    If x < 1: a useful property is ln(1/x)=-ln(x)
    If x > e: a useful property is ln(x/e) = ln(x)-ln(e) --> ln(x)=ln(x/e)+1
    '''
    if(x<1):
        return (-loge(1.0/x))
    if(x>math.e):
        return (loge(x/e)+1.0)
    
    #Binary Search Approach
    lo=0.0
    hi=1.0

    while(True):
        mid=(lo+hi)/2.0
        val= math.exp(mid)
        if (val>x):
            hi=mid
        if(val<x):
            lo=mid
        if (my_abs(val-x)<error):
            return round(mid,error_decimals)

if __name__ == "__main__":            
    test=-1      
    print(loge(test))
    print(math.log(test))   