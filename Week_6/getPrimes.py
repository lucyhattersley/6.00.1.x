def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2 
        yield next
        fibn_2 = fibn_1
        fibn_1 = next
        
def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def genPrime():
    primes = [1, 2, 3]
    next = primes[-1]+1
    isPrime = False
    while isPrime == False:
        for i in range(3, next):
            if next % i == 0:
                next += 1
            else:
                isPrime = True
                primes.append(next)
                yield next
