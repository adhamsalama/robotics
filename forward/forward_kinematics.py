import math
from forward.A_matrix import A_matrix
import numpy as np


def forward_kinematics(*args, **kwargs):
    number_of_joints = int(input('Number of joints: '))
    matrices = []
    for i in range(number_of_joints):
        a, alpha, d, theta = [float(i) for i in input(
            f'Enter a, alpha, d, theta for joint {i + 1}: ').split(' ')]
        matrices.append(A_matrix(a, alpha, d, theta))
    A = multiply_matrices([a.matrix for a in matrices])
    A = np.round(A, decimals=3)
    print("\nT = \n", A)
    end_effector_position(A)


def end_effector_position(T):
    n = len(T) - 1
    p = []
    for i in range(n):
        p.append(T[i][n])
    print("\nXe Ye Ze :", p)

    first_col = []
    last_row = []
    for i in range(n):
        first_col.append(T[i][0])
    for i in range(n):
        last_row.append(T[n - 1][i])

    angl = []
    theta = - \
        math.degrees(math.atan2(last_row[0], math.sqrt(
            1 - math.pow(last_row[0], 2))))
    angl.append(theta)

    phi = math.degrees(math.atan2(first_col[1], first_col[0]))
    angl.append(phi)

    epsi = math.degrees(math.atan2(last_row[1], last_row[2]))
    angl.append(epsi)

    for i in range(len(angl)):
        angl[i] %= 360
    print("Θ, Φ, Ψ : ", angl)


def multiply_matrices(matrices):
    result = matrices[0]
    n = len(matrices)
    for i in range(1, n):
        result = np.dot(result, matrices[i])
    return result
