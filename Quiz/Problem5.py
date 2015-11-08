def primesList(N):
    '''
    N: an integer
    '''
    # Your code here
    primes = []
    for number in range(2, N+1):
        prime = True
        for i in range(2, number):
            if (number % i==0 ):
                prime = False
        if prime:
            primes.append(number)
    return primes

correct_output = [2, 3, 5, 7, 11]

primes = primesList(11)
print "Primes"
print "------"
print primes

print "Correct output"
print "------"
print correct_output

print "True or False match"
print "------"
print primes == correct_output