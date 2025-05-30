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

def aritmetic_op(op, expr1, expr2):
    if callable(expr1) and callable(expr2):
        return lambda x: aritmetics[op](expr1(x), expr2(x))

def relacional_op(op, expr1, expr2):
    if callable(expr1) and callable(expr2):
        return lambda x: relacionals[op](expr1(x), expr2(x))

def apply_unary_op(op, expr):
    # print(f"[DEBUG] apply_unary_op: op={op[0]}, expr={expr}")
    if op[1:] == ':':
        return double_op(op[0], expr)
    if op[1:] == '/':
        return fold_op(op[0], expr)