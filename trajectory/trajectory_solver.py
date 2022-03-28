from inverse.symMatrixA import symMatrixA
from inverse.RollPithYaw import RollPithYaw
from inverse.inverse_kinematics import multiplyMatrices
from sympy import *

# x, y, x', y'
x_val = []
y_val = []
xx_val = []
yy_val = []


def trajectory(*args, **kwargs):
    robotArrangement = input('Enter the robot arrangement (eg. RRP): ')
    A_Matrices = []
    for i in range(len(robotArrangement)):
        if (robotArrangement[i] == 'R' or robotArrangement[i] == 'r'):
            a, alpha, d = [float(i) for i in input(
                f'Enter a, alpha, d for joint {i + 1}: ').split(' ')]
            newTheta = symbols(f'θ{i + 1}')
            theta = newTheta
        if (robotArrangement[i] == 'P' or robotArrangement[i] == 'p'):
            a, alpha, theta = [float(i) for i in input(
                f'Enter a, alpha, θ for joint {i + 1}: ').split(' ')]
            newD = symbols(f'd{i + 1}')
            d = newD
        A_Matrices.append(symMatrixA(a, alpha, d, theta))
    homoT = multiplyMatrices([a.matrix for a in A_Matrices])

    Xe, Ye, Ze, Φ, θ, Ψ = [float(i) for i in input(
        f'Enter End-effector pose (Xe, Ye, Ze, Φ, θ, Ψ): ').split(' ')]

    RBY = RollPithYaw(Φ, θ, Ψ)
    x_equation = sympify(input('Enter the x equation: '))
    y_equation = sympify(input('Enter the y equation: '))
    interval_list = input('Enter the interval: ').strip().split(' ')
    table = [] * len(interval_list)
    solve_equation(x_equation, y_equation, interval_list)
    for interval in range(len(interval_list)):
        table.append({
            't': interval_list[interval],
            'x': x_val[interval],
            'y': y_val[interval],
            'x_dot': xx_val[interval],
            'y_dot': yy_val[interval]
        })

    for i in range(len(table)):
        print(table[i])


def solve_equation(expX, expY, interval_list):
    t = symbols('t')

    # expX differentiation
    exp_difX = diff(expX, t)
    # expY differentiation
    exp_difY = diff(expY, t)

    # substitution by interval list
    for i in range(len(interval_list)):
        x_val.append(expX.subs(t, float(interval_list[i]) * pi / 180))
        y_val.append(expY.subs(t, float(interval_list[i]) * pi / 180))
        xx_val.append(exp_difX.subs(t, float(interval_list[i]) * pi / 180))
        yy_val.append(exp_difY.subs(t, float(interval_list[i]) * pi / 180))

    print('\nexpression X after differentiation: ', format(exp_difX))
    print('expression Y after differentiation: ', format(exp_difY))

