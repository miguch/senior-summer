from sympy import *
from format_latex import *
import mpmath

t1,t2,l1,l2,dott1,dott2=symbols('t1 t2 l1 l2 dott1 dott2')

vx=-((l1*cos(t1)+l2*sin(t1+t2))*dott1)-l2*sin(t1+t2)*dott2
t11, t12,t13,t21,t22,t23 = symbols('t11 t12 t13 t21 t22 t23')
st1,st2,ct1,st12,ct12 = symbols('st1,st2,ct1,st12,ct12')
sqrt2,sqrt3 = symbols('sqrt2 sqrt3')

vx = -(l1*st1+l2*st12)*dott1-l2*st12*dott2
casex1 = vx.subs({
    st1: 0.5,
    st12: -0.5,
    l1: 0.5,
    l2: 0.5
})
casex2 = vx.subs({
    st1: 0.5,
    st12: 0.5,
    l1: 0.5,
    l2: 0.5
})
casex3 = vx.subs({
    st1: 0.5,
    st12: 0,
    l1: 0.5,
    l2: 0.5
})
print(casex1)
print(casex2)
print(casex3)

vx = (l1*ct1+l2*ct12)*dott1+l2*ct12*dott2
# sqrt3 = 3**0.5
casey1 = vx.subs({
    ct1: sqrt3/2,
    ct12: sqrt3/2,
    l1: 0.5,
    l2: 0.5
})
casey2 = vx.subs({
    ct1: sqrt3/2,
    ct12: -sqrt3/2,
    l1: 0.5,
    l2: 0.5
})
casey3 = vx.subs({
    ct1: sqrt3/2,
    ct12: 1,
    l1: 0.5,
    l2: 0.5
})
print(casey1)
print(casey2)
print(casey3)

res = solve([casex1+1, casey1], dict=True)
print(res)

res = solve([casex2, casey2-1], dict=True)
print(res)

res = solve([casex3-1, casey3-1], dict=True)
print(res)

dott1 = ct12/(l1 * st2)
dott2 = -(ct1/(l2*st2))-(ct12/(l1*st2))
print(dott1.subs({
    ct12: sqrt3/2,
    l1: 0.5,
    st2: -sqrt3/2
}))

print(dott2.subs({
    ct1: sqrt3/2,
    l2: 0.5,
    st2: -sqrt3/2,
    ct12: sqrt3/2,
    l1: 0.5
}))

print(dott1.subs({
    ct12: -sqrt3/2,
    l1: 0.5,
    st2: sqrt3/2
}))

print(dott2.subs({
    ct1: sqrt3/2,
    l2: 0.5,
    st2: sqrt3/2,
    ct12: -sqrt3/2,
    l1: 0.5
}))

print(dott1.subs({
    ct12: 1,
    l1: 0.5,
    st2: -0.5
}))

print(dott2.subs({
    ct1: sqrt3/2,
    l2: 0.5,
    st2: -0.5,
    ct12: 1,
    l1: 0.5
}))
