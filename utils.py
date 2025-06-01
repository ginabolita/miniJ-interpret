import numpy as np

UNARY_OPERATORS = [
    '_',  # Negación
    ']',  # Identidad
    'i.',  # Secuencia (0 hasta n-1)
    '#',  # Longitud
    '+:',  # Duplicar suma
    '-:',  # Duplicar resta
    '*:',  # Duplicar multiplicación
    '%:',  # Duplicar división
    '|:',  # Duplicar módulo
    '^:',  # Duplicar potencia
    '+/',  # Fold suma
    '-/',  # Fold resta
    '*/',  # Fold multiplicación
    '%/',  # Fold división
    '|/',  # Fold módulo
    '^/'  # Fold potencia
]

BINARY_OPERATORS = [
    '+',  # Suma
    '-',  # Resta
    '*',  # Multiplicación
    '%',  # División
    '|',  # Módulo
    '^',  # Potencia
    '>',  # Mayor que
    '<',  # Menor que
    '>=',  # Mayor o igual que
    '<=',  # Menor o igual que
    '=',  # Igual que
    '<>',  # Distinto que
    ',',  # Concatenación
    '@:',  # Operador especial
    '{',  # Indexación
    '#',  # Filtrado (especial en binario)
    '+~',  # Suma conmutada
    '-~',  # Resta conmutada
    '*~',  # Multiplicación conmutada
    '%~',  # División conmutada
    '|~',  # Módulo conmutado
    '^~',  # Potencia conmutada
    '>~',  # Mayor que conmutado
    '<~',  # Menor que conmutado
    '>=~',  # Mayor o igual que conmutado
    '<=~',  # Menor o igual que conmutado
    '=~',  # Igual que conmutado
    '<>~',  # Distinto que conmutado
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
    # Cas especial per la concatenació
    if op == '@:':
        # Si és una llista o array, convertim per assegurar la concatenació
        if isinstance(left, (list, np.ndarray)) or isinstance(right, (list, np.ndarray)):
            return list(np.atleast_1d(left)) + list(np.atleast_1d(right))
        else:
            # Si no, fem una llista amb els dos elements
            return [left, right]
    
    # Convertim a arrays per les operacions
    left_arr = np.atleast_1d(left) if not isinstance(left, np.ndarray) else left
    right_arr = np.atleast_1d(right) if not isinstance(right, np.ndarray) else right
    
    # Operacions especials
    if op == '#':
        # Comprovem longituds compatibles
        if len(left_arr) != len(right_arr) and len(left_arr) != 1 and len(right_arr) != 1:
            raise ValueError("Ep! '#' necessita llistes de la mateixa longitud.")
        return right_arr[left_arr.astype(bool).tolist()]
    
    elif op == '{':
        # Indexació
        return right_arr[left_arr]
    
    # Operacions normals
    if op in aritmetics:
        result = aritmetics[op](left_arr, right_arr)
    elif op in relacionals:
        result = relacionals[op](left_arr, right_arr).astype(int)
    else:
        raise ValueError(f"No conec l'operació: {op}")
    
    # Convertim el resultat si cal
    if isinstance(result, np.ndarray):
        return result.tolist()
    return result

def apply_unary_operation(op, expr):
    # print(f"[D]: Applying unary operation '{op}' on {expr}")
    if op in unary_ops:
        r = unary_ops[op](expr)
        return r
    elif op[1:] == ':':
        return apply_binary_operation(op[0], expr, expr)
    elif op[1:] == '/':
        return fold_op(op[0], expr)
