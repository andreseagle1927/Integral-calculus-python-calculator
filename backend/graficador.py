import streamlit as st
import plotly.graph_objects as go
import numpy as np
from sympy import *

def graficar_ejercicio(ecuaciones, marker, x_min, x_max, y_min, y_max):
    x, y = symbols('x y')
    fig = go.Figure()
    for i in range(len(ecuaciones)):
        f = lambdify((x,y), ecuaciones[i], "numpy")
        x_vals = np.linspace(x_min, x_max, 1000)
        y_vals = np.zeros_like(x_vals) # inicializa y_vals como un array de ceros
        y_vals = f(x_vals, y_vals) # asigna los valores de f(x_vals, y_vals) a y_vals
        fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', line=dict(color=np.random.choice(['red', 'blue', 'green', 'purple', 'orange'])), 
                                 marker=dict(symbol=marker), name=f"Ecuación {i+1}"))
    fig.update_layout(title='Graficador', xaxis_title='x', yaxis_title='y', xaxis=dict(range=[x_min, x_max]), yaxis=dict(range=[y_min, y_max]))
    st.plotly_chart(fig)
    fig.show()



def main():
    # Título de la página
    st.title("Graficador de ecuaciones")

    # Descripción de la aplicación

    with st.expander("Instrucciones"):
        st.write("Esta es una aplicación que permite graficar hasta 5 ecuaciones a la vez, sigue estos pasos")
        st.write("1. Ingresa hasta 5 ecuaciones para graficar.")
        st.write("2. Selecciona el número de ecuaciones que deseas graficar.")
        st.write("3. Personaliza los límites del eje x e y del gráfico.")
        st.write("4. Elige el tipo de marcador para cada ecuación.")
        st.write("5. Presiona el botón 'Graficar' para visualizar las ecuaciones.")


    # Definición de las casillas de entrada para las ecuaciones
    ecuacion_1 = st.text_input("Ecuación 1: ", value="x**2")
    ecuacion_2 = st.text_input("Ecuación 2: ", value="sin(x)")
    ecuacion_3 = st.text_input("Ecuación 3: ", value="cos(x)")
    ecuacion_4 = st.text_input("Ecuación 4: ", value="exp(x)")
    ecuacion_5 = st.text_input("Ecuación 5: ", value="log(x)")



    # Determinación del número de ecuaciones que se van a graficar
    num_ecuaciones = st.slider('Número de ecuaciones a graficar', 1, 5, 1)

    # Lista de las ecuaciones que se van a graficar
    ecuaciones = []
    if num_ecuaciones >= 1:
        ecuaciones.append(ecuacion_1)
    if num_ecuaciones >= 2:
        ecuaciones.append(ecuacion_2)
    if num_ecuaciones >= 3:
        ecuaciones.append(ecuacion_3)
    if num_ecuaciones >= 4:
        ecuaciones.append(ecuacion_4)
    if num_ecuaciones >= 5:
        ecuaciones.append(ecuacion_5)

    # Permite al usuario elegir el tipo de marcador para cada ecuación.
    marker = st.selectbox("Selecciona el tipo de marcador para cada ecuación:", ['circle', 'square', 'diamond', 'cross', 'x'])

    # Permite al usuario ingresar límites de eje personalizados para el gráfico.
    x_min, x_max = st.slider("Límites del eje x:", -20, 20, (-10, 10))
    y_min, y_max = st.slider("Límites del eje y:", -20, 20, (-10, 10))

    # Botón para graficar las ecuaciones
    if st.button("Graficar"):
        graficar_ejercicio(ecuaciones, marker, x_min, x_max, y_min, y_max)




