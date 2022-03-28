from unittest import result
from forward.A_matrix import A_matrix
import numpy as np
from jacobian.jacobian_function import calc_jacobian

def inverse_jacobian():
    robotArrangement = input('Enter the robot arrangement (eg. RRP): ')
    matrices = []
    
    for i in range(len(robotArrangement)):
        a, alpha, d, theta = [float(i) for i in input(
            f'Enter a, alpha, d, theta for joint {i+1}: ').split(' ')]
        matrices.append(A_matrix(a, alpha, d, theta))
    
    result = calc_inverse_jacobian(robotArrangement , matrices)
    for i in range(len(robotArrangement)):
        for j in range(6):
            print(result[i][j], end='\t')
        print()
        
        
def calc_inverse_jacobian(robotArrangement , matrices):
    jac = calc_jacobian(robotArrangement , matrices)
    jacT = rotate(jac, len(robotArrangement))
    jacTdotJac = np.dot(jacT, jac)
    inverseJacobianResult = np.dot(jacTdotJac,jacT)
    inverseJacobianResult = np.round(inverseJacobianResult, decimals=3)
    return inverseJacobianResult


def rotate(matrix, n):
    ret = []
    for i in range(n):
        ret.append([])
    for i in range(6):
        for j in range(n):
            ret[j].append(matrix[i][j])
    return ret