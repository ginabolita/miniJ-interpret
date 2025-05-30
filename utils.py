import numpy as np
from antlr4 import *

aritmetics = {
    '+': np.add,
    '-': np.subtract,
    '*': np.multiply,
    '%': np.divide,
    '|': np.mod,
    '^': np.power,
    ',': np.append,
}

relacionals = {
    '>': np.greater,
    '<': np.less,
    '>=': np.greater_equal,
    '<=': np.less_equal,
    '=': np.equal,
    '<>': np.not_equal
}

#######################
## OPERADORS UNARIS ##
#######################
def identity_op(expr):
    return expr

def negate_op(expr):
    return -expr

def size_op(expr):
    return np.array([len(expr)])

def n_primers(n):
    return np.arange(n)

def double_op(op, expr):
    if op in aritmetics:
        return aritmetics[op](expr, expr)

def fold_op(op, expr):
    result = expr[0]
    for i in range(1, len(expr)):
        result = aritmetics[op](result, expr[i])
    return result

def apply_unary_op(op, expr):
    print(f"[DEBUG] apply_unary_op: op={op[0]}, expr={expr}")
    if op[1:] == ':':
        return double_op(op[0], expr)
    if op[1:] == '/':
        return fold_op(op[0], expr)
    if op == 'i.':
        return n_primers(expr)
    if op == ']':
        return identity_op(expr)
#######################
## OPERADORS BINARIS ##
#######################
def concatenate_op(left, right):
    return np.append(left, right)

def index_op(left, right):
    return right[left]

def mask_op(left, right):
    return right[left.astype(bool)]

def flip_op(op, left, right):
    if isinstance(left, np.ndarray) and left.size == 1:
        left = left.item()
    if isinstance(right, np.ndarray) and right.size == 1:
        right = right.item()
    if op in aritmetics:
        print(
            f"[DEBUG] apply_flip_binop: flip operation {op} with expressions: {left}, {right}"
        )
        return aritmetic_op(op, left, right)
    else:
        raise ValueError(f"Operador desconegut: {op}")

def aritmetic_op(op, left, right):
    return aritmetics[op](left, right)

def relacional_op(op, left, right):
    if callable(left) and callable(right):
        return lambda x: relacionals[op](left(x), right(x))

def apply_binary_op(op, left, right):
    print(f"[DEBUG] apply_binary_op: op={op[0]}, left={left}, right={right}")
    # if op == '@:':
    # if op == '|':
    # if op in relacionals:
    # if op in aritmetics:
