###for i in range(2, 11, 2):
###    print i
###print "Goodbye!"
###
###print "Hello!"
###for i in range(10, 1, -2):
###    print i
##
###end = 6
###
###amount = 0
###for i in range(1, end+1):
###    amount += i
###print amount
##
###iteration = 0
###count = 0
###while iteration < 5:
###    # the variable 'letter' in the loop stands for every 
###    # character, including spaces and commas!
###    for letter in "hello, world": 
###        count += 1
###    print "Iteration " + str(iteration) + "; count is: " + str(count)
###    iteration += 1 
###    
##iteration = 0
##while iteration < 5:
##    count = 0
##    for letter in "hello, world":
##        count += 1
##    print "Iteration " + str(iteration) + "; count is: " + str(count)
##    iteration += 1 
##    
##iteration = 0
##while iteration < 5:
##    count = 0
##    for letter in "hello, world":
##        count += 1
##        if iteration % 2 == 0:
##            break
##    print "Iteration " + str(iteration) + "; count is: " + str(count)
##    iteration += 1 
#
##iteration = 0
##count = 0
##while iteration < 5:
##    for letter in "hello, world":
##        count += 1
##    print "Iteration " + str(iteration) + "; count is: " + str(count)
##    iteration += 1 
#
#x = 25
#epsilon = 0.01
#step = 0.1
#guess = 0.0
#
#while guess <= x:
#    if abs(guess**2 -x) >= epsilon:
#        guess += step
#
#if abs(guess**2 - x) >= epsilon:
#    print 'failed'
#else:
#    print 'succeeded: ' + str(guess)

x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)