from sympy import *
import numpy as np
from format import to_latex

tn, an, dn, alphan = symbols('tn an dn alphan')
mat1 = Matrix([[cos(tn),-sin(tn),0,0],[sin(tn),cos(tn),0,0],[0,0,1,0],[0,0,0,1]])
mat2 = Matrix([[1,0,0,an],[0,1,0,0],[0,0,1,dn],[0,0,0,1]])
mat3 = Matrix([[1,0,0,0],[0,cos(alphan),-sin(alphan),0],[0,sin(alphan),cos(alphan),0],[0,0,0,1]])

print(mat1*mat2*mat3)

result = mat1*mat2*mat3
l1,t1,t2,d2 = symbols('l1 t1 t2 d2')
A1 = result.subs({
    alphan: 0,
    an: 0,
    dn: 0,
    tn: t1
    })
A2 = result.subs({
    alphan: 0,
    an: d2,
    dn: 0,
    tn: 0
    })

print(to_latex(A1*A2))
