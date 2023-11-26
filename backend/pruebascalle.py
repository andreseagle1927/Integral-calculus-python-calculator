import re
from numpy import matrix




def get_matrix_expression(expression, matrix_dict):
    # Reemplazar todas las operaciones en las que una matriz está elevada a una potencia con la matriz original
    expression = re.sub(r"\b[A-Za-z]+\^[A-Za-z]+\b", lambda m: m.group(0).split("^")[0], expression)

    # Reemplazar todas las operaciones en las que una matriz está transpuesta con la matriz original
    expression = re.sub(r"\b[A-Za-z]+\^T\b", lambda m: m.group(0).split("^")[0], expression)

    # Reemplazar todas las operaciones en las que una matriz está en la diagonal con la matriz original
    expression = re.sub(r"\b[A-Za-z]+\|D\b", lambda m: m.group(0).split("|")[0], expression)

    # Reemplazar todas las operaciones en las que una matriz está en la zona triangular superior con la matriz original
    expression = re.sub(r"\b[A-Za-z]+\^Z\b", lambda m: m.group(0).split("^")[0], expression)

    # Reemplazar el patrón "A=L" con solo "A"
    expression = re.sub(r"\b[A-Za-z]+\=L\b", lambda m: m.group(0).split("=")[0], expression)


    # Buscar patrones en la cadena de operación matricial
    patterns = [r"\b[A-Za-z]+\b"]
    patterns.append(r"\d*\.\d+|\d+")
    patterns.append(r"\s+")
    patterns.append(r"[\+\-\*/\(\)]+")
    patterns.append(r"\b[A-Za-z]+\w*\b")

    regex = re.compile("|".join(patterns))

    # Reemplazar cada matriz por su nombre
    def replace(match):
        s = match.group(0)
        if s in matrix_dict:
            return s
        else:
            return s

    replaced = regex.sub(replace, expression)

    # Devolver la cadena de operación matricial
    return replaced.strip()


def matrix_operation_dict(matrix_dict, operation):
    for name, matrix in matrix_dict.items():
        globals()[name] = matrix
    try:
        result = eval(operation)
    except:
        raise ValueError("La operación matricial es inválida.")
    return result

expression = "a + b"
matrix_dict = {'a': matrix([[-0.33333333,  0.66666667],
        [ 0.66666667, -0.33333333]]), 'b': matrix([[-0.33333333,  0.66666667],
        [ 0.66666667, -0.33333333]])}


result = get_matrix_expression(expression, matrix_dict)
print(result)
a=matrix_operation_dict(matrix_dict,result)
print(a)
