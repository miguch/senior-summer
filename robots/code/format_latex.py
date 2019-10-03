from sympy import *
from collections.abc import Iterable

def to_latex(mat):
    row, col = mat.shape
    result = ''
    for r in range(row):
        for c in range(col):
            result += str(mat[r,c])
            result += '&'
        result += '\\\\'
    result = '\\begin{bmatrix}' + result + '\\end{bmatrix}'
    return result

def to_latex_var(mat):
    #4x4
    result = '\\begin{bmatrix} n_x&o_x&a_x&p_x\\n_y&o_y&a_y&p_y\\n_z&o_z&a_z&p_z\\0&0&0&1 \\end{bmatrix}\n\n'
    vars_name = ['n','o','a','p']
    axis_name = ['x','y','z']
    for r in range(3):
        for c in range(4):
            result += '$' + vars_name[c] + '_' + axis_name[r] + ' = ' + str(mat[r,c])
            result += '$\n'
    return result