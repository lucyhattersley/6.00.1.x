def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    amount = 0
    for i in aDict.keys():
        amount += len(aDict[i])
    return amount