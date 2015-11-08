def isPrime(n):
    import math
    if n == 1:
        return True
    elif n == 2:
        return True
    else:
        for i  in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

def genPrimes():
    import math
    primes = []
    candidate = 1
    while True:
        candidate += 1
        for i in primes:
            if candidate % i == 0:
                break
        else:
            primes.append(candidate)
            yield candidate
            
#Write a generator, genPrimes, that returns the sequence of prime numbers
#on successive calls to its next() method: 2, 3, 5, 7, 11, ...

def genPrimes2():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last

p = genPrimes()