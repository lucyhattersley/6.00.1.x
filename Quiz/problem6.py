def count7(N):
    '''
    N: a non-negative integer
    '''
    # Your code here  
    count = 0
    if N > 0:
        if N % 10 == 7:
            count += 1
        return count7(N / 10)
    return count