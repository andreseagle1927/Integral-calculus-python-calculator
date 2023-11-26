import streamlit as st
import sympy
import pandas as pd

def calcular_solucion(matriz_aumentada):
    A = sympy.Matrix(matriz_aumentada)
    forma_reducida, pivotes = A.rref()
    x = forma_reducida[:, -1]
    soluciones = []
    for i in range(x.shape[0]):
        soluciones.append(("x{}".format(i+1), x[i]))
    return forma_reducida.tolist(), soluciones
def maingauss():
    st.title("Gauss jordan")
    with st.expander("ℹ️ Instrucciones"):
        st.write("Esta es una calculadora Gauss-Jordan para resolver sistemas de ecuaciones lineales.")
        st.write("Para utilizarla, sigue los siguientes pasos:")
        st.write("1. Selecciona el tamaño de la matriz utilizando el control deslizante.")
        st.write("   - El tamaño representa el número de incógnitas en el sistema de ecuaciones.")
        st.write("2. Ingresa los valores de las ecuaciones en los campos de input.")
        st.write("   - Cada fila representa una ecuación.")
        st.write("   - El último valor en cada fila corresponde al término independiente.")
        st.write("3. Haz clic en 'Calcular' para resolver el sistema de ecuaciones.")
        st.write("   - Se mostrará la solución en la columna de la izquierda.")
        st.write("   - Los valores de las incógnitas se mostrarán redondeados a una cifra decimal.")
        st.write("   - La matriz resuelta se mostrará en la columna de la derecha.")

    # Pedir el tamaño de la matriz al usuario
    tamano = st.slider("Seleccione el tamaño de la matriz", min_value=2, max_value=5)

    # Crear una matriz de ceros con el tamaño especificado
    matriz = [[0 for _ in range(tamano+1)] for _ in range(tamano)]

    # Crear dos columnas para los inputs
    col1, col2 = st.columns(2)

    # Pedir los valores de la matriz al usuario
    for i in range(tamano):
        for j in range(tamano+1):
            if j == tamano:
                input_text = "Ingrese el valor independiente de la linea {}".format(i+1)
            else:
                input_text = "Ingrese el vector {}  x{}".format(i+1, j+1)
            if j <= tamano//2:
                matriz[i][j] = col1.number_input(input_text, key=(i,j))
            else:
                matriz[i][j] = col2.number_input(input_text, key=(i,j))

    # Calcular la solución al hacer clic en el botón "Calcular"
    if st.button("Calcular"):
        # Crear dos columnas para los resultados
        col3, col4 = st.columns(2)
        with col3:
            matriz_resuelta, soluciones = calcular_solucion(matriz)
            for variable, valor in soluciones:
                st.write("{} = {:.1f}".format(variable, round(valor, 1)))
        with col4:
            # Redondear valores independientes en la matriz
            matriz_redondeada = [[round(valor, 1) for valor in fila] for fila in matriz_resuelta]
            # Convertir matriz redondeada en DataFrame y mostrar tabla
            resultadito = pd.DataFrame(matriz_redondeada)
            resultadito.index = resultadito.index + 1  # Suma 1 a cada índice
            resultadito.columns = resultadito.columns + 1
            st.table(resultadito)
