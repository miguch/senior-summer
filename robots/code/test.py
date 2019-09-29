from sympy import *
import numpy as np

tn, an, dn, alphan = symbols('tn an dn alphan')
mat1 = np.array([[cos(tn),-sin(tn),0,0],[sin(tn),cos(tn),0,0],[0,0,1,0],[0,0,0,1]])
mat2 = np.array([[1,0,0,an],[0,1,0,0],[0,0,1,dn],[0,0,0,1]])
mat3 = np.array([[1,0,0,0],[0,cos(alphan),-sin(alphan),0],[0,sin(alphan),cos(alphan),0],[0,0,0,1]])

print(mat1.dot(mat2).dot(mat3))


result = mat1.dot(mat2).dot(mat3)
