#def applyFuns(L, x):
#    for f in L:
#        print(f(x))
#
#applyFuns([abs, int], -4.4)

testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
#def addOne(input):
#    return input + 1
#    
#applyToEach(testList, addOne)

def absSquared(input):
    return abs(input * input)

applyToEach(testList, absSquared)

print testList