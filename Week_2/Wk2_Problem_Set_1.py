#s = 'valar morghulis'
#
#vowelCount = 0
#
#for char in s:
#    if char in 'aeiou':
#        vowelCount += 1
#
#print 'Number of vowels: ' + str(vowelCount)
#

#Find bob
# Take one. Didn't work
# print "Number of times bob occurs is: " + str(s.count('bob'))


#s = 'ttoboonobobooobobbobkobobnsbobbaoo'
#index = 0
#bobCount = 0
#
#while index < len(s):
#    if s[index:index+3] == 'bob':
#        bobCount += 1
#    index += 1
#    
#print "Number of times bob occurs is: " + str(bobCount)
   
    
# should find beggh
#         
#index1 = ''
#index2 = ''
#
#for char in s:
#    if (index1 == ''):
#        index1 = char
#    elif (index1[-1] <= char):
#        index2 += char
#    elif (index2[-1] > char):
#        if (len(index1) < len(index2)):
#            index1 = index2
#            index2 = char
#        else:
#            index2 = char
#if (len(index2) > len(index1)):
#    index1 = index2
#print(index1)
#
#print "Longest substring in alphabetical order is: " + index1
#    

s = 'azcbobobegghakl'

substring = {}
max_value = 0

for i in range(len(s)):
    count = 0
    sub_value  = s[i]

    while i+1 < len(s) and s[i] <= s[i+1]:
        count += 1
        i += 1
        sub_value += s[i]

    substring[count] = substring.get(count, sub_value)
    max_value = max(substring.keys())
    
print('Longest substring in alphabetical order is: ' + substring[max_value])