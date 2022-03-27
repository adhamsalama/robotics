from sympy import *
class symMatrixA():
    def __init__(self, a, alpha, d, theta):
    
        if type(theta) == float:
            ci = N(cos(theta*pi/180),5) # theta
            si = N(sin(theta *pi/180),5) # theta
        else:
            ci = cos(theta) # theta
            si = sin(theta) # theta
        if type(alpha) == float:
            ca = N(cos(alpha *pi/180),5) # alpha
            sa = N(sin(alpha*pi/180),5)  # alpha
        else :
            ca = cos(alpha) # alpha
            sa = sin(alpha)  # alpha
        
        self.matrix = Array([
            [ci, -si*ca,
             si*sa, a*ci],

            [si, ci*ca,
             -ci*sa, a*si],

            [0, sa,ca, d],

            [0, 0, 0, 1]
        ])