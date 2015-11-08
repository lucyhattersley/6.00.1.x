def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    handLen = 0
    for letter in hand.keys():
        for j in range(hand[letter]):
             handLen += 1
    return handLen

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':2}
print calculateHandlen(hand)