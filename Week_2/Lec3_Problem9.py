print("Please think of a number between 0 and 100!")

high = 100
low = 0

guess = (high + low) / 2
status = ""
correct = False

while correct == False:
    print "Is your secret number " + str(guess) + "?"
    status = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if status == 'c':
        correct = True
    elif status == 'h':
        high = guess
        guess = (low + high) / 2
    elif status == 'l':
        low = guess
        guess = (low + high) / 2
    else:
        print "Sorry, I did not understand your input." 
print "Game over. Your secret number was: " + str(guess)