import string
import numpy as np
from math import sin, cos, pi
import sympy as sp

class inverse_matrix():
    def __init__(self, a, alpha, d, theta):
    
        if type(theta) == int:
            ci = sp.cos(theta*pi/180).round(3) # theta
            si = sp.sin(theta *pi/180).round(3) # theta
        else:
            ci = sp.cos(theta) # theta
            si = sp.sin(theta) # theta
        if type(alpha) == int:
            ca = sp.cos(alpha *pi/180).round(3) # alpha
            sa = sp.sin(alpha*pi/180).round(3)  # alpha
        else :
            ca = sp.cos(alpha) # alpha
            sa = sp.sin(alpha)  # alpha
        
        self.matrix =sp.Array([
            [ci, -si*ca,
             si*sa, a*ci],

            [si, ci*ca,
             -ci*sa, a*si],

            [0, sa,ca, d],

            [0, 0, 0, 1]
        ])