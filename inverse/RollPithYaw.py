from sympy import *

class RollPithYaw():
    def __init__(self,Φ,θ,Ψ):
        cΦ = cos(Φ*pi/180).round(3) 
        sΦ = sin(Φ *pi/180).round(3) 
    
        cθ = cos(θ*pi/180).round(3)
        sθ = sin(θ*pi/180).round(3) 
        
        cΨ = cos(Ψ *pi/180).round(3) # alpha
        sΨ = sin(Ψ*pi/180).round(3)  # alpha
        
        self.matrix = Array([
            [cΦ*cθ, -sΦ*cΨ+cΦ*sθ*sΨ,
             sΦ*sΨ+cΦ*sθ*cΨ],
            [sΦ*cθ, cΦ*cΨ+sΦ*sθ*sΨ,
             -cΦ*sΨ+sΦ*sθ*cΨ],
            [-sθ, cθ*sΨ,cθ*cΨ],
        ])