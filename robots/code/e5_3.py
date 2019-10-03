from sympy import *
import numpy as np
import mpmath
from format_latex import *

tn, an, dn, alphan = symbols('tn an dn alphan')
mat1 = Matrix([[cos(tn),-sin(tn),0,0],[sin(tn),cos(tn),0,0],[0,0,1,0],[0,0,0,1]])
mat2 = Matrix([[1,0,0,an],[0,1,0,0],[0,0,1,dn],[0,0,0,1]])
mat3 = Matrix([[1,0,0,0],[0,cos(alphan),-sin(alphan),0],[0,sin(alphan),cos(alphan),0],[0,0,0,1]])

print(mat1*mat2*mat3)

trans = mat1*mat2*mat3
t1,t2,t3,t4,t5,t6,a2,a3,d2,d4 = symbols('t1 t2 t3 t4 t5 t6 a2 a3 d2 d4')

params = [
    [0,0,0,t1],
    [mpmath.radians(-90),0,d2,t2],
    [0,a2,0,t3],
    [mpmath.radians(-90),a3,d4,t4],
    [mpmath.radians(90),0,0,t5],
    [mpmath.radians(-90),0,0,t6]
]
# params = [
#     [0,0,0,mpmath.radians(90)],
#     [mpmath.radians(-90),0,d2,0],
#     [0,a2,0,mpmath.radians(-90)],
#     [mpmath.radians(-90),a3,d4,0],
#     [mpmath.radians(90),0,0,0],
#     [mpmath.radians(-90),0,0,0]
# ]
mats = []
for param in params:
    A = N(trans.subs({
        alphan: param[0],
        an: param[1],
        dn: param[2],
        tn: param[3]
        }))
    A = Matrix(A)
    nsimplify(A,tolerance=1e-10,rational=True)
    mats.append(A)
    print(to_latex(A))

print(to_latex_var(mats[0]*mats[1]*mats[2]*mats[3]*mats[4]*mats[5]))
