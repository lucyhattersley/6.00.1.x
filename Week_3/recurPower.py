#def recurPower(base, exp):
#    '''takes two numbers, base and exp
#    recursively calls itself to provide result'''
#    if exp == 0:
#        return 1
#    elif exp == 1:
#        return base
#    else:
#        return base * recurPower(base, exp-1)

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp <= 0:
        return 1
    elif exp % 2 == 0:
        return recurPowerNew(base*base, (exp / 2))
    else:
        return base * recurPowerNew(base, (exp -1))