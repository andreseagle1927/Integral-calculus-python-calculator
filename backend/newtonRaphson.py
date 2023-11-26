import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
from sympy import sympify, lambdify, symbols,diff

# Function to calculate the root using the Newton-Raphson method


def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
    iteraciones = []
    x = x0

    for i in range(max_iter):
        fx = f(x)
        fx_prime = f_prime(x)
        x_next = x - fx / fx_prime
        error = abs(x_next - x)
        iteraciones.append({"x0": x, "raiz": x_next, "error": error})
        if abs(x_next - x) < tol:
            return x_next, iteraciones
        x = x_next

    raise ValueError(
        f"El método de Newton-Raphson no converge después de {max_iter} iteraciones")


# Function to read the equation


def read_equation(equation_str):
    try:
        x = symbols('x')
        equation = sympify(equation_str)
        func = lambdify(x, equation, modules=['numpy'])
        return func
    except Exception as e:
        error_type = type(e).__name__
        error_msg = str(e)
        print(f"Error: La ecuación no es válida. {error_type}: {error_msg}")
        st.markdown("""
            <style>
            .big-font {
                font-size:20px !important;
                text-align: left;
            }
            </style>
            """, unsafe_allow_html=True)
        st.markdown(
            f'<h1 class="big-font">Error: La ecuación no es válida. {error_type}: {error_msg}</h1>', unsafe_allow_html=True)
        return None




def main():
    try:
        # Title
        st.markdown("<h1 style='text-align: center; color: #218c74;'>Método de newton raphson</h1>", unsafe_allow_html=True)
        st.write("<hr>", unsafe_allow_html=True)

        with st.expander("Instrucciones"):
                st.write("Ingrese una ecuación matemática utilizando la variable x. Puede utilizar operadores matemáticos como +, -, *, / y ** para indicar sumas, restas, multiplicaciones, divisiones y potencias, respectivamente. También puede utilizar funciones matemáticas comunes como sin(), cos(), tan(), exp(), log(), etc. Asegúrese de que la función esté escrita en términos de la variable x.")
                st.write("- La ecuación debe ser una función de una variable.")
                st.write("- El punto inicial x0 debe estar lo suficientemente cerca de la raíz.")
                st.write("- La función y su primera derivada deben ser continuas en el intervalo.")
                st.write("- La tolerancia debe ser un número positivo.")
                st.write("- El número máximo de iteraciones debe ser un número entero positivo.")
        # Input equation
        # Input equation
        equation_str = st.text_input("Ecuación", "(sin(x)/x) + cos(1+x**2) - 0.2", help="Ingrese una ecuación matemática usando la variable x. Puede usar operadores matemáticos como +, -, *, /, y ** para indicar sumas, restas, multiplicaciones, divisiones y potencias respectivamente. También puede utilizar funciones matemáticas comunes como sin(), cos(), tan(), exp(), log(), etc. Recuerde que la función debe estar escrita en términos de la variable x.")

        # Input initial values
        x0 = st.number_input("Valor inicial x0", value=1.0, help="Ingrese un valor inicial para la variable x.")


        # Read equation
        f = read_equation(equation_str)

        # Calculate derivative
        x = symbols('x')
        f_prime = lambdify(x, diff(sympify(equation_str), x))

    except:
        # Print error message
        st.warning("Error: Incorrectos los datos a evaluar.")
        return

    # Create button to calculate the root
    if st.button("Calcular"):

        # Create try except to catch errors
        try:
            # Calculate root approximation
            raiz, iteraciones = newton_raphson(f, f_prime, x0=x0)

            # Print success message
            st.success("La raíz es {} después {} iteraciones.".format(
                raiz, len(iteraciones)))
        except:
            # Print error message
            st.warning("Error: Defina correctamente los datos a evaluar.")
            return

        # Create table with iterations
        columnas = ["Iteración", "x0", "raiz", "f(raiz)", "error"]
        datos = []

        for i, iteracion in enumerate(iteraciones):
            datos.append([i+1, iteracion["x0"], iteracion["raiz"],
                         f(iteracion["raiz"]), abs(iteracion["error"])])
        tabla_df = pd.DataFrame(datos, columns=columnas)

        # Plot function and root approximation
        x = np.linspace(0, 3, 100)
        y = f(x)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="f(x)"))
        fig.add_shape(
            type="line",
            x0=0,
            y0=0,
            x1=3,
            y1=0,
            line=dict(color="gray", dash="dash"),
        )
        fig.add_trace(go.Scatter(x=[raiz], y=[f(raiz)], mode="markers", marker=dict(
            color="red"), name="Aproximación de la raíz"))
        fig.update_layout(title="Gráfica de la función f(x) y su aproximación de la raíz",
                          xaxis_title="x", yaxis_title="f(x)")

        # Show plot
        st.plotly_chart(fig)

        # expander
        expander = st.expander("Tabla de iteraciones")

        # Show table
        expander.table(tabla_df)
