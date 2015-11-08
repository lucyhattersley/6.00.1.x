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
            count = 0
            for item in aDict:
                if aDict[item] == value:
                    count += 1
            if count == 1:
                uniqueKeys.append(key)
        return uniqueKeys
