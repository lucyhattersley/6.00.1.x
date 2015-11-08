def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    newL = []
    for s in L:
        if f(s) == True:
            newL.append(s)
    L[:] = newL
    return len(L)
    

run_satisfiesF(L, satisfiesF)

def f(s):
    return 'a' in s
      
#L = ['a', 'b', 'a']
#print satisfiesF(L)
#print L

#L = ['a', 'b', 'd']
#print satisfiesF(L)
#print L
#
#L = ['foo', 'fii', 'fah']
#print satisfiesF(L)
#print L
#
#L = []
#print satisfiesF(L)
#print L
#
#L = ['a', 'bah', 'aaa']
#print satisfiesF(L)
#print L

L = ['a', 'aa', 'bbb']
print satisfiesF(L)
print L