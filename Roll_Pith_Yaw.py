import string
import numpy as np
from math import sin, cos, pi
import sympy as sp

class Roll_Pith_Yaw():
    def __init__(self,Φ,θ,Ψ):
    
        
        cΦ = sp.cos(Φ*pi/180).round(3) 
        sΦ = sp.sin(Φ *pi/180).round(3) 
    
        cθ = sp.cos(θ*pi/180).round(3)
        sθ = sp.sin(θ*pi/180).round(3) 
        
        cΨ = sp.cos(Ψ *pi/180).round(3) # alpha
        sΨ = sp.sin(Ψ*pi/180).round(3)  # alpha
        
        
        self.matrix =sp.Array([
            [cΦ*cθ, -sΦ*cΨ+cΦ*sθ*sΨ,
             sΦ*sΨ+cΦ*sθ*cΨ],

            [sΦ*cθ, cΦ*cΨ+sΦ*sθ*sΨ,
             -cΦ*sΨ+sΦ*sθ*cΨ],

            [-sθ, cθ*sΨ,cθ*cΨ],

            
        ])