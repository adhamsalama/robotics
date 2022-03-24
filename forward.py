from A_matrix import A_matrix
import numpy as np


def forward(*args, **kwargs):
    number_of_joints = int(input('Number of joints: '))
    matrices = []
    for i in range(number_of_joints):
        a = float(input(f'a for {i+1}th joint: '))
        alpha = float(input(f'alpha for {i+1}th joint: '))
        d = float(input(f'd for {i+1}th joint: '))
        theta = float(input(f'theta for {i+1}th joint: '))
        matrices.append(A_matrix(a, alpha, d, theta))
    A = multiply_matrices([a.matrix for a in matrices])
    print(np.round(A, decimals=3))


def multiply_matrices(matrices):
    result = matrices[0]
    n = len(matrices)
    for i in range(1, n):
        result = np.dot(result, matrices[i])
    return result
