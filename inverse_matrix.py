import numpy as np
from math import sin, cos, pi
import sympy as sp

class inverse_matrix():
    def __init__(self, a, alpha, d, theta):
    
        self.matrix =sp.Array([
            [sp.cos(theta*pi/180), -sp.sin(theta*pi/180)*sp.cos(alpha*pi/180),
             sp.sin(theta*pi/180)*sp.sin(alpha*pi/180), a*sp.cos(theta*pi/180)],

            [sp.sin(theta*pi/180), sp.cos(theta*pi/180)*sp.cos(alpha*pi/180),
             -sp.cos(theta*pi/180)*sp.sin(alpha*pi/180), a*sp.sin(theta*pi/180)],

            [0, sp.sin(alpha*pi/180),sp. cos(alpha*pi/180), d],

            [0, 0, 0, 1]
        ])