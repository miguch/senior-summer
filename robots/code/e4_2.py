from sympy import *
from format_latex import *
import mpmath

g,sqrt3=symbols('g sqrt3')
j = Matrix([[-0.4*sqrt3-0.4, -0.4,-0.4], [1.2,0.8,0]])
f = Matrix([[0],[10*g]])
print(transpose(j), f, transpose(j)*f)

