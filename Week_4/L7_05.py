def foo(x, a):
   """
   x: a positive integer argument
   a: a positive integer argument

   returns an integer
   """
   count = 0
   while x >= a:
      count += 1
      print "Count is: " + str(count)
      x = x - a
   print "Path B"
   return count
 