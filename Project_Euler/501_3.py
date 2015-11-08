def divLen(number):
    divs = []
    for i in range(1,number+1):
        if number % i == 0:
            divs.append(i)
    return len(divs)

def findEights(number):
    eights = 0
    for i in range(1, number):
        if divLen(number) == 8:
            eights == 1
    return eights

print findEights(100)