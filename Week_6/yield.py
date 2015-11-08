import math

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

def gen_primes():
    primes = [1, 2, 3]
    candidate = primes[-1]+1
    while True:
        for i in range(3, int(math.sqrt(candidate) + 1), 2):
            if candidate % i == 0:
                pass
            else:
                yield candidate
                primes.append(candidate)
            candidate += 1
        
        
def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number
        number += 1

def print_successive_primes(iterations, base=10):
    prime_generator = get_primes(base)
    prime_generator.send(None)
    for power in range


#def get_primes(number):
#    while True:
#        if is_prime(number):
#            yield number
#        number += 1

def solve_number_10():
    total = 2
    for next_prime in get_primes(3):
        if next_prime  < 2000000:
            total += next_prime
        else:
            print(total)
            return

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False
    
def simple_generator_function():
    yield 1
    yield 2
    yield 3

