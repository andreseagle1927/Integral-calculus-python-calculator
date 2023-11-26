import streamlit as st
from sympy import Matrix
import numpy as np
import pandas as pd
import re

from backend.gauss_jordan import maingauss
# Define el número máximo de matrices que se pueden almacenar
MAX_MATRICES = 30

# Crea un diccionario para almacenar las matrices y sus nombres
matrices = {}

def add_matrix(matrix, name):
    try:
        if len(matrices) < MAX_MATRICES:
            matrices[name] = matrix
        else:
            st.warning(f"Solo se pueden almacenar {MAX_MATRICES} matrices")
    except:
        st.warning("No se pudo agregar la matriz. Intente de nuevo más tarde.")


# Obtiene la expresión de operación matricial sin los nombres de las matrices
def get_matrix_expression(expression, matrix_dict):

    try:

   

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
    except:
        st.warning("No se pudo obtener la expresión de operación matricial. Intente de nuevo más tarde.")

def matrix_operation_dict(matrix_dict, operation):
    try:
        for name, matrix in matrix_dict.items():
            globals()[name] = matrix
        result = eval(operation)
    except:
        st.warning("La operación matricial es inválida. Intente de nuevo con una operación válida.")
    return result


def matrix_operation(operation, matrices_to_use):
    try:
        result = eval(operation, {}, matrices_to_use)
        df = pd.DataFrame(result)
        df.index = df.index + 1  # Suma 1 a cada índice
        df.columns = df.columns + 1
        return df
    except:
        st.warning("No se pudo realizar la operación matricial. Intente de nuevo con una operación válida.")


def matrix_ingreso(num_rows, num_cols):
    try:
        matrix = []
        half_cols = num_cols // 2
        for i in range(num_rows):
            row = []
            col1, col2 = st.columns(2)
            for j in range(half_cols):
                row.append(col1.number_input(f"Enter value for row {i+1}, column {j+1}", key=f"matrix[{i}][{j}]"))
            for j in range(half_cols, num_cols):
                row.append(col2.number_input(f"Enter value for row {i+1}, column {j+1}", key=f"matrix[{i}][{j}]"))
            matrix.append(row)
        return matrix
    except:
        st.warning("No se pudo obtener la matriz ingresada. Intente de nuevo con valores numéricos válidos.")


def lu_factorization(matrix):
    try:
        n = len(matrix)
        L = np.identity(n)
        U = np.zeros((n, n))
        for k in range(n):
            U[k, k] = matrix[k, k] - np.dot(L[k, :k], U[:k, k])
            for i in range(k + 1, n):
                L[i, k] = (matrix[i, k] - np.dot(L[i, :k], U[:k, k])) / U[k, k]
            for j in range(k + 1, n):
                U[k, j] = matrix[k, j] - np.dot(L[k, :k], U[:k, j])
        return L, U
    except:
         st.warning("No se puede realizar la factorización LU de la matriz ingresada. Intente con una matriz cuadrada.")



    
# Elimina una matriz del diccionario
def remove_matrix(name):
    try:
        matrices.pop(name, None)
    except:
        st.warning("No se pudo eliminar la matriz. Intente de nuevo más tarde.")


# Función para obtener la inversa de una matriz
def inverse_matrix(matrix):
    """
    Obtiene la inversa de una matriz.
    """
    try:
        result = matrix.I
        return result
    except:
        st.warning("No se puede obtener la inversa de la matriz ingresada. Intente con una matriz cuadrada y no singular.")



# Función para obtener la transposición de una matriz
def transpose_matrix(matrix):
    """
    Obtiene la transposición de una matriz.
    """
    try:
        result = np.transpose(matrix)
        return result
    except:
        st.warning("Error: No se puede obtener la transposición de la matriz ingresada.  Intente con una matriz válida.")


# Función para obtener la factorización LU de una matriz
def factorize_matrix(matrix):
    try:
        L, U = lu_factorization(matrix)
        return L, U
    except Exception as e:
        st.error(f"Se ha producido un error al calcular la factorización LU: {e}")

# Función para obtener el determinante de una matriz
def determinant_matrix(matrix):
    try:
        result = np.linalg.det(matrix)
        return result
    except Exception as e:
        st.error(f"Se ha producido un error al calcular el determinante: {e}")

# Función para obtener la diagonal de una matriz
def diagonal_matrix(matrix):
    try:
        result = np.diag(matrix)
        return result
    except Exception as e:
        st.error(f"Se ha producido un error al obtener la diagonal de la matriz: {e}")


def get_matrix(diccionario):
    try:
        # Obtiene una lista de las claves del diccionario
        claves = list(diccionario.keys())
        
        # Selecciona la primera matriz en el diccionario
        matriz = diccionario[claves[0]]
        
        # Convierte la matriz a un objeto NumPy
        matriz_np = np.matrix(matriz)
        
        return matriz_np
    except :
        return diccionario

def operate_matrices(operation, matrices_to_use):
    matrixoperables = {}
    
    def add_matrixoperable(matrix, name):
        matrixoperables[name] = matrix
    
    # Verifica si hay varias suboperaciones separadas por coma o punto y coma
    sub_operations = re.split(r'\s*[\+\-\*/]\s*', operation)
    
    if len(sub_operations) > 1:
        # Si hay varias suboperaciones, llama recursivamente a operate_matrices() para cada una y combina los resultados
        result = {}
        for sub_operation in sub_operations:
            sub_result = operate_matrices(sub_operation.strip(), matrices_to_use)
            if sub_result is None:
                continue
            result.update(sub_result)
        #saca operaicones
        operacionesfinales=get_matrix_expression(operation, result)
        #peor argumento que se puede tener es cuestionar la visibilidad 
        resultadofinal=matrix_operation_dict(result,operacionesfinales)

        return resultadofinal

    # Si solo hay una suboperación, determina el tipo de operación y llama a la función correspondiente
    matrix_names = re.findall(r'[A-Za-z]+\w*(?<!I)(?<!i)(?<!T)(?<!t)(?<!Z)(?<!z)(?<!L)(?<!l)(?<!D)(?<!d)|[A-Za-z]+\w*\^T|[A-Za-z]+\w*\^I|[A-Za-z]+\w*\=L|[A-Za-z]+\w*\|D|[A-Za-z]+\w*\^Z', operation)
    matrices = [matrices_to_use[matrix_name] for matrix_name in matrix_names]

    try:
        if "^I" in operation:
            # Inversa de una matriz
            result = inverse_matrix(matrices[0])
            add_matrixoperable(result, matrix_names[0])
            return {matrix_names[0]: result}

        elif "^T" in operation:
            # Transposición de una matriz
            result = transpose_matrix(matrices[0])
            add_matrixoperable(result, matrix_names[0])
            return {matrix_names[0]: result}

        elif "=L" in operation:
            # Ejemplo de uso
            L, U = factorize_matrix(matrices[0])       
            st.write("Matriz A")
            st.write(matrices[0])
            st.write("Matriz L")
            st.write(L)
            st.write("Matriz U ")
            st.write(U)
            return None

        elif "|D" in operation:
            # Determinante
            result = determinant_matrix(matrices[0])
            add_matrixoperable(result, matrix_names[0])      
            return {matrix_names[0]: result}

        elif "^Z" in operation:
            # Matriz diagonal
            result = diagonal_matrix(matrices[0])
            add_matrixoperable(result, matrix_names[0])      
            return {matrix_names[0]: result}
        
        else:
            return {matrix_names[0]: matrices[0]}
    
    except Exception as e:
        print(f"Ha ocurrido un error: {str(e)}")
        








def mainmatrices():
    st.title("Calculadora de Ecuaciones Matriciales")
    with st.expander("ℹ️ Instrucciones"):
        st.write("Esta es una calculadora de operaciones matriciales.")
        st.write("Para utilizarla, sigue los siguientes pasos:")
        st.write("1. Agrega matrices utilizando el formulario 'Agregar Matriz'.")
        st.write("   - Ingresa un nombre para la matriz.")
        st.write("   - Ingresa los valores de la matriz separados por comas.")
        st.write("   - Haz clic en 'Agregar' para agregar la matriz.")
        st.write("2. Ingresa la operación matricial en el campo 'Operación'.")
        st.write("   - Utiliza los nombres de las matrices agregadas y los operadores correspondientes.")
        st.write("   - Los operadores disponibles incluyen la transposición (^T), la inversa (^I), la factorización LU (=L), el cálculo del determinante (|D) y la obtención de la matriz diagonal (^Z).")
        st.write("3. Haz clic en 'Calcular' para obtener el resultado de la operación.")
        st.write("   - El resultado se mostrará en una tabla.")
        st.write("   - Si hay algún error en la operación, se mostrará un mensaje de error.")
        st.write("4. Utiliza el formulario 'Eliminar Matriz' para eliminar una matriz del conjunto de matrices.")
        st.write("   - Selecciona la matriz que deseas eliminar.")
        st.write("   - Haz clic en 'Eliminar' para eliminar la matriz.")

    with st.expander("Agregar Matriz"):
        name = st.text_input("Nombre de la matriz")
        matrix_str = st.text_area("Matriz (separada por comas)", help="Digita la matriz cada linea separada por un punto y coma, y cada valor separado por comas ")
        if st.button("Agregar"):
            try:
                matrix = np.matrix(matrix_str)
                add_matrix(matrix, name)
                st.success(f"Matriz {name} agregada con éxito")
            except Exception as e:
                st.error(f"Digite una matriz correcta :() el error es : {str(e)}")

    st.subheader("Operar Matrices")
    operation = st.text_input("Operación (ejemplo: A^I + B*A - C)", help="permite realizar diferentes operaciones matriciales en base a una cadena de operaciones. La cadena de operaciones debe contener los nombres de las matrices a utilizar, seguidos de los operadores correspondientes para realizar la operación deseada. Los operadores disponibles incluyen la transposición (^T), la inversa (^I), la factorización LU (=L), el cálculo del determinante (|D) y la obtención de la matriz diagonal (^Z). La función extrae los nombres de las matrices de la cadena de operaciones, las elimina si se duplican y luego obtiene las matrices correspondientes. Luego, realiza la operación deseada en base al operador utilizado y muestra los resultados en la salida.")
    if st.button("Calcular"):
        try:
            resultado = operate_matrices(operation, matrices)
            resultadofinal = get_matrix(resultado)
            resultadito = pd.DataFrame(resultadofinal)
            resultadito.index = resultadito.index + 1  # Suma 1 a cada índice
            resultadito.columns = resultadito.columns + 1
            st.table(resultadito)
        except Exception as e:
            st.error(f"Error al realizar la operación: {str(e)}")

    with st.expander("Eliminar Matriz"):
        matrix_names = list(matrices.keys())
        selected_matrix = st.selectbox("Nombre de la matriz", matrix_names)

        if st.button("Eliminar"):
            remove_matrix(selected_matrix)
            st.success(f"Matriz {selected_matrix} eliminada con éxito")


def mainprofe():
    st.title("Calculadora de Ecuaciones Matriciales")

    # Nombre de la matriz
    name = st.text_input("Ingresa el nombre de la matriz:")

    # Opciones de tamaño
    col1, col2 = st.columns(2)
    with col1:
        num_rows = st.slider("Número de filas", min_value=1, step=1, value=2)
    with col2:
        num_cols = st.slider("Número de columnas", min_value=1, step=1, value=2)

    matrix = matrix_ingreso(num_rows, num_cols)

    if st.button("Agregar1"):
        try:
            matrix = np.matrix(matrix)
            add_matrix(matrix, name)
            st.success(f"Matriz {name} agregada con éxito")
            st.write(f"Matriz {name}:")
            st.table(matrix)
        except Exception as e:
            st.error(str(e))


    # Realiza una operación matricial a través de una caja de texto
    st.subheader("Operar Matrices1")
    operationn = st.text_input("Operación (ejemplo: A^I + B*A - C, ",help="permite realizar diferentes operaciones matriciales en base a una cadena de operaciones. La cadena de operaciones debe contener los nombres de las matrices a utilizar, seguidos de los operadores correspondientes para realizar la operación deseada. Los operadores disponibles incluyen la transposición (^T), la inversa (^I), la factorización LU (=L), el cálculo del determinante (|D) y la obtención de la matriz diagonal (^Z). La función extrae los nombres de las matrices de la cadena de operaciones, las elimina si se duplican y luego obtiene las matrices correspondientes. Luego, realiza la operación deseada en base al operador utilizado y muestra los resultados en la salida.")
    if st.button("Calcular"):
        operate_matrices(operationn)

    # Elimina una matriz del diccionario a través de un botón
    st.subheader("Eliminar Matriz")
    matrix_names = list(matrices.keys())
    selected_matrix = st.selectbox("Nombre de la matriz", matrix_names)
    if st.button("Eliminar1"):
        remove_matrix(selected_matrix)
        st.success(f"Matriz {selected_matrix} eliminada con éxito")

def maindoble():
    col1, col2 = st.columns(2)
    with col1:
        Matrices = st.checkbox('Operaciones matriciales')
        
    with col2:
        Jordan = st.checkbox('Gauss jordan')
    if Jordan:
        maingauss()
    elif Matrices:
        mainmatrices()
if __name__ == '__main__':
    maindoble()
