hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
newHand = {}
word = 'quail'

WORDLIST_FILENAME = "/Users/Lucy/Dropbox/2_active_projects/6001x/ProblemSet4/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    newHand = hand.copy()
    for letter in word:
        newHand[letter] -= 1
    return newHand

print "Original hand: " + str(hand)
print "Word: " + word
newHand = updateHand(hand, word)
print "Updated hand: " + str(newHand)