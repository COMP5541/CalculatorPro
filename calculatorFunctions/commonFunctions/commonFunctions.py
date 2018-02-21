def power(x,y):
    if isinstance(x,(int,float)) and isinstance(y,int):

        if x==0:
          return 0

        if y==0:
            return 1

        # Positive Values
        if y >0:
            return x * power(x, y- 1)

        # Negative Values
        elif not y >0:
            return 1./float(power(x,-y))
    else:
        print ('X must be a number and Y must be an integer')




print (power(2.5,11))