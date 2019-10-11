from sympy import *
from format_latex import *
import mpmath

l1,s1,t1,l2,s12,t2,c1,l2,c12=symbols('l1,s1,t1,l2,s12,t2,c1,l2,c12')

x = -l1*s1*t1-l2*s12*(t1+t2)
y = l1*c1*t1+l2*c12*(t1+t2)

print(x**2+y**2)
