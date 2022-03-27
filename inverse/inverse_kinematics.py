from inverse.symMatrixA import symMatrixA
from inverse.RollPithYaw import RollPithYaw
import numpy as np
from sympy import *
# from math import pi


def inverse_kinematics(*args, **kwargs):

    robotArrangement = input('Enter the robot arrangement (eg. RRP): ')
    A_Matrices = []
    for i in range(len(robotArrangement)):
        if(robotArrangement[i] == 'R' or robotArrangement[i] == 'r'):
            a, alpha, d = [float(i) for i in input(
                f'Enter a, alpha, d for joint {i+1}: ').split(' ')]
            newTheta = symbols(f'θ{i+1}')
            theta = newTheta
        if(robotArrangement[i] == 'P' or robotArrangement[i] == 'p'):
            a, alpha, theta = [float(i) for i in input(
                f'Enter a, alpha, θ for joint {i+1}: ').split(' ')]
            newD = symbols(f'd{i+1}')
            d = newD
        A_Matrices.append(symMatrixA(a, alpha, d, theta))

    homoT = multiplyMatrices([a.matrix for a in A_Matrices])

    Xe, Ye, Ze, Φ, θ, Ψ = [float(i) for i in input(
        f'Enter End-effector pose (Xe, Ye, Ze, Φ, θ, Ψ): ').split(' ')]

    RBY = RollPithYaw(Φ, θ, Ψ)

    # print()

    # print(homoT)
    # print(RBY.matrix)

    # Position matrix equations
    xEq = Eq(homoT[0][3], Xe)
    yEq = Eq(homoT[1][3], Ye)
    zEq = Eq(homoT[2][3], Ze)

    # Rotation matrix equations
    r11Eq = Eq(homoT[0][0], RBY.matrix[0][0])
    r12Eq = Eq(homoT[0][1], RBY.matrix[0][1])
    r13Eq = Eq(homoT[0][2], RBY.matrix[0][2])

    r21Eq = Eq(homoT[1][0], RBY.matrix[1][0])
    r22Eq = Eq(homoT[1][1], RBY.matrix[1][1])
    r23Eq = Eq(homoT[1][2], RBY.matrix[1][2])

    r31Eq = Eq(homoT[2][0], RBY.matrix[2][0])
    r32Eq = Eq(homoT[2][1], RBY.matrix[2][1])
    r33Eq = Eq(homoT[2][2], RBY.matrix[2][2])

    result = solve([xEq, yEq, zEq], dict=True)

    for i in range(len(result)):
        for key, value in result[i].items():
            stringKey = f'{key}'
            if stringKey[0] == 'θ':
                result[i][key] = N(value*180/pi, 5)
            else:
                result[i][key] = N(value, 5)
    print()
    print(result)
    print()

    # counter = 0
    # for i in range(len(homoT)):
    #     for j in range(4):
    #         print(type (homoT[i][j]) != np.number)
    #         print(homoT[i][j].round(2))
    #         counter=counter +1
    # print(counter)


def multiplyMatrices(A_Matrices):
    result = A_Matrices[0]
    n = len(A_Matrices)
    for i in range(1, n):
        result = np.dot(result, A_Matrices[i])
    return result

# Examples:

    # Input:
    # RR
    # [ 2 0 0 ]
    # [ 2 0 0 ]
    # Xe = 2.25  Ye = 2.94
    # Output:
    # [{θ1: 30.323, θ2: 44.499}, {θ1: 74.823, θ2: -44.499}]

    # Input:
    # RPP
    # [ 0 0 0.1 ]
    # [ 0 -90 0 ]
    # [ 0 0 0 ]
    # Xe = -0.1    Ye = 0   Ze = 0.2
    # Output:
    # [{θ1: 270.00, d3: -0.10000, d2: 0.10000}, {θ1: 90.000, d3: 0.10000, d2: 0.10000}]

    # RPP
    # [ 0 0 1 ]
    # [ 0 -90 0 ]
    # [ 0 0 0 ]
    # Xe = 1    Ye = -1.2   Ze = 2
    # θ1 values in degree  = 39.806
    # d2 values in degree = 1.0000
    # d3 values in degree = 1.5620
