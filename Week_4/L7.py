def maxOfThree(a,b,c) :
    """
    a, b, and c are numbers

    returns: the maximum of a, b, and c        
    """
    if a > b:
        bigger = a
        print "Path A"

    else:
        bigger = b
        print "Path B"

    if c > bigger:
        bigger = c
        print "Path C"

    return bigger