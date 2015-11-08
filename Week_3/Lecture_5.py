def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1    
    i = exp-1
    result = base    
    while i > 0:
        result *= base
        i -= 1
    return result
        