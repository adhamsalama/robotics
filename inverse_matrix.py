import numpy as np
from math import sin, cos, pi
import sympy as sp

class inverse_matrix():
    def __init__(self, a, alpha, d, theta):
    
        self.matrix =sp.Array([
            [sp.cos(theta), -sp.sin(theta)*sp.cos(alpha),
             sp.sin(theta)*sp.sin(alpha), a*sp.cos(theta)],

            [sp.sin(theta), sp.cos(theta)*sp.cos(alpha),
             -sp.cos(theta)*sp.sin(alpha), a*sp.sin(theta)],

            [0, sp.sin(alpha),sp. cos(alpha), d],

            [0, 0, 0, 1]
        ])