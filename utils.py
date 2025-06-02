import numpy as np

UNARY_OPERATORS = [
    '_',
    ']',
    'i.',
    '#',
    '+:',
    '-:',
    '*:',
    '%:',
    '|:',
    '^:',
    '+/',
    '-/',
    '*/',
    '%/',
    '|/',
    '^/'
]

BINARY_OPERATORS = [
    '+',
    '-',
    '*',
    '%',
    '|',
    '^',
    '>',
    '<',
    '>=',
    '<=',
    '=',
    '<>',
    ',',
    '@:',
    '{',
    '#',
    '+~',
    '-~',
    '*~',
    '%~',
    '|~',
    '^~',
    '>~',
    '<~',
    '>=~',
    '<=~',
    '=~',
    '<>~',
    ',~',
    '@:~',
    '{~'
]

aritmetics = {
    '+': np.add,
    '-': np.subtract,
    '*': np.multiply,
    '%': np.divide,
    '|': lambda x, y: np.mod(y, x),
    '^': np.power,
    ',': lambda x, y: np.concatenate((np.atleast_1d(x), np.atleast_1d(y))),
}

relacionals = {
    '>': np.greater,
    '<': np.less,
    '>=': np.greater_equal,
    '<=': np.less_equal,
    '=': np.equal,
    '<>': np.not_equal
}

unary_ops = {
    '_': lambda x: -x,
    ']': lambda x: x,
    'i.': lambda x: np.arange(int(x[0]) if isinstance(x, list) else int(x)),
    '#': lambda x: len(np.atleast_1d(x))
}

def fold_op(op, expr):
    result = expr[0]
    for i in range(1, len(expr)):
        result = aritmetics[op](result, expr[i])
    return result

def apply_binary_operation(op, left, right):
    if op == '@:':  # Composició
        return list(np.atleast_1d(left)) + list(np.atleast_1d(right))
    left_arr = np.atleast_1d(left) if not isinstance(left,
                                                     np.ndarray) else left
    right_arr = np.atleast_1d(right) if not isinstance(right,
                                                       np.ndarray) else right
    size_exempt_ops = ['@:', ',', '{']
    if (op not in size_exempt_ops and
        len(left_arr.shape) > 0 and len(right_arr.shape) > 0 and
        left_arr.shape != right_arr.shape and
        left_arr.size != 1 and right_arr.size != 1):
        raise ValueError(
            f"Error operació binària: diferent mida - {left_arr.shape} i {right_arr.shape}"
        )
    if op == '#':  # Màscara
        if len(left_arr) != len(right_arr) and len(left_arr) != 1 and len(
                right_arr) != 1:
            raise ValueError(
                "Error! '#' necessita llistes de la mateixa mida.")
        return right_arr[left_arr.astype(bool).tolist()]

    elif op == '{':  # IndexacióMàscara
        return right_arr[left_arr]

    if op in aritmetics:
        result = aritmetics[op](left_arr, right_arr)
    elif op in relacionals:
        result = relacionals[op](left_arr, right_arr).astype(int)
    else:
        raise ValueError(f"Error! Operació desconeguda: {op}")

    if isinstance(result, np.ndarray):
        return result.tolist()
    return result

def apply_unary_operation(op, expr):
    if op in unary_ops:
        r = unary_ops[op](expr)
        return r
    elif op[1:] == ':':
        # print(f"debug: {op} {expr}")
        return apply_binary_operation(op[0], expr, expr)
    elif op[1:] == '/':
        return fold_op(op[0], expr)
