import numpy as np

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


def check_length(left, right):
    left_len = len(left)
    right_len = len(right)

    if left_len == right_len:
        return False

    if left_len == 1 or right_len == 1:
        return False

    return True


def fold_op(op, expr):
    result = expr[0]
    for i in range(1, len(expr)):
        result = aritmetics[op](result, expr[i])
    return result


def apply_binary_operation(op, left, right):
    left_arr = np.atleast_1d(left) if not isinstance(left,
                                                     np.ndarray) else left
    right_arr = np.atleast_1d(right) if not isinstance(right,
                                                       np.ndarray) else right

    if op == '#':
        if check_length(left_arr, right_arr):
            raise ValueError(
                "Operació '#' només es pot aplicar a llistes de la mateixa longitud."
            )
        return right_arr[left_arr.astype(bool).tolist()]
    elif op == '{':
        return right_arr[left_arr]
    if op in aritmetics:
        result = aritmetics[op](left_arr, right_arr)
    elif op in relacionals:
        result = relacionals[op](left_arr, right_arr).astype(int)
    else:
        raise ValueError(f"Operació desconeguda: {op}")

    return result.tolist() if isinstance(result, np.ndarray) else result


def apply_unary_operation(op, expr):
    if op in unary_ops:
        return unary_ops[op](expr)
    elif op[1:] == ':':
        return apply_binary_operation(op[0], expr, expr)
    elif op[1:] == '/':
        return fold_op(op[0], expr)

