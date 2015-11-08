def isPal(number):
    num1 = number
    num2 = 0
    while num1 > 0:
        digit = num1 % 10
        num2 = (num2 * 10) + digit
        num1 = num1 / 10
    return number == num2


largestNum = 0

for i in range(111,999):
   for x in range(111, 999):
      num = i * x
      if isPal(num):
          if num > largestNum:
              largestNum = num

print "The largest palindrome made from two three digit numbers is: " + str(largestNum)