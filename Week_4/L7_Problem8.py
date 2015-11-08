def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      print n
      return 1
   else:
      print n
      return n * f(n-1)