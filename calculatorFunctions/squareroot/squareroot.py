def squareroot( value):

    error = 0.00000000001
    squareRootVal = value/2
    if value == 0:
        return 0

    if value == 1:
        return 1


    while True:
        dif = squareRootVal**2 - value

        if abs(dif) <= error:
            break

        squareRootVal = (squareRootVal + value / squareRootVal) / 2.0
    return squareRootVal


