from A_matrix import A_matrix
import numpy as np


def forward(*args, **kwargs):
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

    col = []
    row = []
    for i in range(n):
        col.append(T[i][0])
    for i in range(n):
        row.append(T[n - 1][i])

    tan_phi = col[1] / col[0] if col[0] else 0
    tan_theta = row[0] / math.sqrt(1-math.pow(row[0], 2)) if row[0] else 0
    tan_epsi = row[1] / row[2] if row[2] else 0

    phi = math.degrees(math.atan(tan_phi))
    theta = math.degrees(math.atan(tan_theta))
    epsi = math.degrees(math.atan(tan_epsi))

    print("\nΦ =", np.round(phi, 3))
    print("Θ =", np.round(theta, 3))
    print("Ψ =", np.round(epsi, 3))
    
    

def multiply_matrices(matrices):
    result = matrices[0]
    n = len(matrices)
    for i in range(1, n):
        result = np.dot(result, matrices[i])
    return result
