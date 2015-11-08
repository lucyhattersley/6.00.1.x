#def square(x):
#    return x * x
#    
#def fourthPower(x):
#    return square(x) * square(x)
#    
#def odd(x):
#    return x % 2 != 0

#def isVowel(char):
#    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#    count = 0
#    while count < len(vowels):
#        if char == vowels[count]:
#            return True
#        count += 1
#    return False

def isVowel2(char):
    if char in 'aeiou':
        return True
    else:
        return False