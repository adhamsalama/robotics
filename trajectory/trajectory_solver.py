from curses import A_DIM
from inverse.symMatrixA import symMatrixA
from inverse.RollPithYaw import RollPithYaw
from inverse.inverse_kinematics import multiplyMatrices
from inverse.inverse_kinematics import solveInverseKinematics
from sympy import *
from forward.A_matrix import A_matrix
from inverse_jacobian.inverse_jacobian_function import calc_inverse_jacobian, rotate
import numpy as np

# x, y, x', y'
x = []
y = []
z = []
xDot = []
yDot = []
zDot = []
θ1 = []
θ2 = []
θ1Dot = []
θ2Dot = []

def trajectory(*args, **kwargs):
    params = []
    robotArrangement = input('Enter the robot arrangement (eg. RRP): ')
    A_Matrices = []
    for i in range(len(robotArrangement)):
        if (robotArrangement[i] == 'R' or robotArrangement[i] == 'r'):
            a, alpha, d = [float(i) for i in input(
                f'Enter a, alpha, d for joint {i + 1}: ').split(' ')]
            newTheta = symbols(f'θ{i + 1}')
            theta = newTheta
            params.append([a,alpha,d])
        if (robotArrangement[i] == 'P' or robotArrangement[i] == 'p'):
            a, alpha, theta = [float(i) for i in input(
                f'Enter a, alpha, θ for joint {i + 1}: ').split(' ')]
            newD = symbols(f'd{i + 1}')
            d = newD
        A_Matrices.append(symMatrixA(a, alpha, d, theta))

    homoT = multiplyMatrices([a.matrix for a in A_Matrices])
    
    x_equation = sympify(input('Enter the x equation: '))
    y_equation = sympify(input('Enter the y equation: '))
    interval_list = input('Enter the interval: ').strip().split(' ')
    table = [] * len(interval_list)

    solve_equation(x_equation, y_equation, interval_list)
    
    getJointAngels(homoT, interval_list)
    
    for interval in range(len(interval_list)):
        calc_θDot(params, interval)
    
    for interval in range(len(interval_list)):
        table.append({
            't': interval_list[interval],
            'x': x[interval],
            'y': y[interval],
            'θ1': θ1[interval],
            'θ2': θ2[interval],
            'x_dot': xDot[interval],
            'y_dot': yDot[interval],
            'θ1_dot': θ1Dot[interval],
            'θ2_dot': θ2Dot[interval]
        })
    
    a0,a1,a2,a3, t= symbols('a0 a1 a2 a3 t')
    ax=np.array([θ1[0][0],θ1Dot[0][0],a2,a3])
    ax = ax.transpose()
    e = [[1,0,0,0],[0,1,0,0],
    [1,pi/8,np.power(pi,2)/64,np.power(pi,3)/512],
    [0,1,pi/4,np.power(pi,2)*3/64]
    ]
    res = np.dot(e,ax)
    a0 = N(θ1[0][0],5)
    a1 = N(θ1Dot[0][0],5)
    eq1 = Eq(res[2],θ1[1][0])
    eq2 = Eq(res[3],θ1Dot[1][0])
    r = solve([eq1,eq2],[a2,a3])
    a2 = N(r[a2],5)
    a3 = N(r[a3],5)

    b0,b1,b2,b3, t= symbols('b0 b1 b2 b3 t')
    ax=np.array([θ2[0][0],θ2Dot[0][0],b2,b3])
    resθ2 = np.dot(e,ax)
    b0 = N(θ2[0][0],5)
    b1 = N(θ2Dot[0][0],5)
    eq1θ2 = Eq(resθ2[2],θ2[1][0])
    eq2θ2 = Eq(resθ2[3],θ2Dot[1][0])
    rθ2 = solve([eq1θ2,eq2θ2],[b2,b3])
    b2 = N(rθ2[b2],5)
    b3 = N(rθ2[b3],5)
    for i in range(len(table)):
        print(table[i])
    print(f'θ1(t) ={a0+a1*t+a2*np.power(t,2),+a3*np.power(t,3)}')
    print(f'θ2(t) ={b0+b1*t+b2*np.power(t,2),+b3*np.power(t,3)}')



        
def solve_equation(expX, expY, interval_list):
    t = symbols('t')

    # expX differentiation
    exp_difX = diff(expX, t)
    # expY differentiation
    exp_difY = diff(expY, t)

    # substitution by interval list
    for i in range(len(interval_list)):
        x.append(N(float(expX.subs(t, float(interval_list[i]) * pi / 180)),5))
        y.append(N(float(expY.subs(t, float(interval_list[i]) * pi / 180)),5))
        xDot.append(N(float(exp_difX.subs(t, float(interval_list[i]) * pi / 180)),5))
        yDot.append(N(float(exp_difY.subs(t, float(interval_list[i]) * pi / 180)),5))

def getJointAngels(homoT, interval_list):
    # substitution by interval list
    for i in range(len(interval_list)):
        firstAngle = []
        secondAngle = []
        # Position matrix equations
        xEq = Eq(homoT[0][3], x[i])
        yEq = Eq(homoT[1][3], y[i])
        # zEq = Eq(homoT[2][3], z[i])
        result = solveInverseKinematics([xEq,yEq])

        for i in range(len(result)):
            for key, value in result[i].items():
                stringKey = f'{key}'
                if stringKey == 'θ1':
                    firstAngle.append(result[i][key])
                else:
                    secondAngle.append(result[i][key])
        θ1.append(firstAngle)
        θ2.append(secondAngle)
        
def calc_θDot(params,i):
    θ1Dot.append([])
    θ2Dot.append([])
    zeta = [[xDot[i]],[yDot[i]],[0],[0],[0],[0]]
    matrices = []
    matrices.append(A_matrix(params[0][0],params[0][1],params[0][2], θ1[i][0]))
    matrices.append(A_matrix(params[0][0],params[0][1],params[0][2], θ2[i][0]))
    invJac = calc_inverse_jacobian('rr',matrices)
    ret = np.dot(invJac, zeta)
    θ1Dot[i].append(N(ret[0][0],5))
    θ2Dot[i].append(N(ret[1][0],5))
    matrices = []
    matrices.append(A_matrix(params[0][0],params[0][1],params[0][2], θ1[i][1]))
    matrices.append(A_matrix(params[0][0],params[0][1],params[0][2], θ2[i][1]))
    invJac = calc_inverse_jacobian('rr',matrices)
    ret = np.dot(invJac, zeta)
    θ1Dot[i].append(N(ret[0][0],5))
    θ2Dot[i].append(N(ret[1][0],5))