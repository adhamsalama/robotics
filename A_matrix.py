import numpy as np
from math import sin, cos, pi


class A_matrix():
    def __init__(self, a, alpha, d, theta):
        self.matrix = np.array([
            [cos(theta*pi/180), -sin(theta*pi/180)*cos(alpha*pi/180),
             sin(theta*pi/180)*sin(alpha*pi/180), a*cos(theta*pi/180)],

            [sin(theta*pi/180), cos(theta*pi/180)*cos(alpha*pi/180),
             -cos(theta*pi/180)*sin(alpha*pi/180), a*sin(theta*pi/180)],

            [0, sin(alpha*pi/180), cos(alpha*pi/180), d],

            [0, 0, 0, 1]
        ])
