divisors = []

def findDivs(number):
    if number % i == 0:
        divisors.append(i)
    return divisors + findDivs(i+1, number)