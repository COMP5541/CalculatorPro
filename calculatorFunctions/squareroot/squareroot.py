def squareroot( value):

    if (value == 0 or value == 1):
        return value

    # Look for the square root using binary search
    start = 1
    end = value
    while (start <= end):
        mid = (start + end) // 2

        if (mid * mid == value):
            return mid

        if (mid * mid < value):
            start = mid + 1
            ans = mid

        else:
            end = mid - 1


    return ans