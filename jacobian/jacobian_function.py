from forward.A_matrix import A_matrix
import numpy as np

def jacobian():
    robotArrangement = input('Enter the robot arrangement (eg. RRP): ')
    matrices = []
    
    for i in range(len(robotArrangement)):
        a, alpha, d, theta = [float(i) for i in input(
            f'Enter a, alpha, d, theta for joint {i+1}: ').split(' ')]
        matrices.append(A_matrix(a, alpha, d, theta))
    jac = calc_jacobian(robotArrangement , matrices)
    for i in range(6):
        for j in range(len(robotArrangement)):
            print(jac[i][j], end='\t')
        print()

def calc_jacobian(robotArrangement, matrices):
    postionVector = genPositionVector([a.matrix for a in matrices])
    zVector = genZVector([a.matrix for a in matrices])
    jac = []
    for i in range(6):
        jac.append([])
    n = len(robotArrangement)
    for i in range(n):
        jv = []
        if robotArrangement[i] == 'R' or robotArrangement[i] == 'r':
            jv = np.cross(zVector[i], (postionVector[n]-postionVector[i]))
            for j in range(3):
                jac[j].append(round(jv[j], 3))
            for j in range(3, 6):
                jac[j].append(round(zVector[i][j-3], 3))
        if robotArrangement[i] == 'P' or robotArrangement[i] == 'p':
            for j in range(3):
                jac[j].append(round(zVector[i][j], 3))
            for j in range(3, 6):
                jac[j].append(0)
    for i in range(len(jac)):
        for j in range(len(jac[0])):
            jac[i][j] += 0
    return jac


def multiply_matrices(matrices):
    result = matrices[0]
    n = len(matrices)
    for i in range(1, n):
        result = np.dot(result, matrices[i])
    return result


def genZVector(matrices):
    Z = [np.array([0, 0, 1])]
    result = matrices[0]
    Z.append(np.array([result[0, 2], result[1, 2], result[2, 2]]))
    n = len(matrices)
    for i in range(1, n-1):
        result = np.dot(result, matrices[i])
        Z.append(np.array([result[0, 2], result[1, 2], result[2, 2]]))
    return Z


def genPositionVector(matrices):
    O = [np.array([0, 0, 0])]
    result = matrices[0]
    O.append(np.array([result[0, 3], result[1, 3], result[2, 3]]))
    n = len(matrices)
    for i in range(1, n):
        result = np.dot(result, matrices[i])
        O.append(np.array([result[0, 3], result[1, 3], result[2, 3]]))
    return O

