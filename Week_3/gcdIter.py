def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
     Your code here
    if a <= b:
        smallerInteger = a
    else:
        smallerInteger = b
    for i in range(smallerInteger,0,-1):
        if i == 1:
            return 1
        elif a % i == 0 and b % i == 0:
            return i
