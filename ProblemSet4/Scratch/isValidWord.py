hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
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

def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if word not in wordList:
        return False
    
    allLetters = []
    for letter in hand.keys():
        for j in range(hand[letter]):
             allLetters += letter
    
    wordFine = False
    for letter in word:
        if letter in allLetters:
            allLetters.remove(letter)
            wordFine = True
        else:
            wordFine = False
            break
    print "Returning wordFine"
    return wordFine
        
if __name__ == '__main__':
    wordList = loadWords()
    isValidWord(word, hand, wordList)