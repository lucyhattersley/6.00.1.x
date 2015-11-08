def genFib():
    fibn_1 = 1
    fibn_2 = 0
    while True:
        next = fibn_1 + fibn_2
        yield next
        fibn_1 = fibn_2
        fibn_2 = next
        
def genPrimes