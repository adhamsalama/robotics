from inverse_matrix import inverse_matrix
import numpy as np
import sympy as sp
from math import pi, radians 

def inverse(*args, **kwargs):
    
    
    θ1,θ2,θ3,θ4,θ5,θ6,d1,d2,d3,d4,d5,d6=sp.symbols('θ1 θ2 θ3 θ4 θ5 θ6 d1 d2 d3 d4 d5 d6')
    arrangment= input('Enter the robot arrangment: ')
    matrices = []
    for i in range(len(arrangment)):
        if(arrangment[i]=='R' or arrangment[i]=='r'):
            a, alpha, d = [int(i) for i in input(
            f'Enter a, alpha, d for joint {i+1}: ').split(' ')]
            
            if(i+1==1):
                theta = θ1
                
            if(i+1==2):
                theta = θ2
            if(i+1==3):
                theta = θ3
            if(i+1==4):
                theta = θ4
            if(i+1==5):
                theta = θ5
            if(i+1==6):
                theta = θ6
        if(arrangment[i]=='P' or arrangment[i]=='p'):
            a, alpha, theta = [int(i) for i in input(
            f'Enter a, alpha, θ for joint {i+1}: ').split(' ')]
             
            if(i+1==1):
                d = d1
            if(i+1==2):
                d = d2
            if(i+1==3):
                d = d3
            if(i+1==4):
                d = d4
            if(i+1==5):
                d = d5
            if(i+1==6):
                d = d6
        matrices.append(inverse_matrix(a, alpha, d, theta))

    A = multiply_matrices([a.matrix for a in matrices])
    print(A)
    
    # counter = 0
    # for i in range(len(A)):
    #     for j in range(4):
    #         print(type (A[i][j]) != np.number)
    #         print(A[i][j].round(2))
    #         counter=counter +1
    # print(counter)
    
    
   
    
        
        

def multiply_matrices(matrices):
    result = matrices[0]
    n = len(matrices)
    for i in range(1, n):
        result = np.dot(result, matrices[i])
    return result
        