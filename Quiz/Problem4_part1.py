a1 = 8.72
b1 = -8.49
c1 = -4.32
x1 = 3.2
a2 = 9.85
b2 = 4.83
c2 = 6.1
x2 = -4.07


def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    return (a*(x**2))+(b*x)+c
    
def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    # Your code here  
    print evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2)

twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2)