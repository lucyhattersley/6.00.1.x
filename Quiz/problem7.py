def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    if aDict == {}:
        return([])
    
    elif len(aDict) == 1:
        return[(aDict.keys()[0])]
    
    else:
        uniqueKeys = []
        for key in aDict:
            value = aDict[key]
            count = dictCount(aDict, value)
            if count == 1:
                uniqueKeys.append(key)
        return uniqueKeys

  
def dictCount(aDict, n):
    '''
    Accepts a key:value dictionary and an integer.
    Counts how many times the integer appears as a value
    Returns the count
    '''
    count = 0
    for key in aDict:
        if aDict[key] == n:
            count += 1
    return count
