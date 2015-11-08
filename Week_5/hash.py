import string

def hash(s):
    return string.ascii_lowercase.index(s[0])
    
import string

def hash2(s):
    return string.ascii_lowercase.index(s[-1])
    
def hash3(s):
    total = 0
    for char in s:
        total += string.ascii_lowercase.index(char)
    return total % 26