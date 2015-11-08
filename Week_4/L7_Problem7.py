def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
        print("Route A")
    elif x < a:
        return x
        print("Route B")
    else:
        return rem(x-a, a)
        print("Route C")