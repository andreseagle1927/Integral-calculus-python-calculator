import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
from sympy import sympify, lambdify, symbols

# Function to read the equation
def read_equation(equation_str):
    """
    Parsea una cadena de texto con una ecuación y devuelve una función que la evalúa.
    """
    try:
        x = symbols('x')
        equation = sympify(equation_str)
        func = lambdify(x, equation)
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
        st.markdown(f'<h1 class="big-font">Error: La ecuación no es válida. {error_type}: {error_msg}</h1>', unsafe_allow_html=True)
        return None

# Function to calculate the bisection method
def bisection(f, a, b, tolerance=1e-6, max_iterations=100, safety_factor=1.5):
    if f(a) * f(b) > 0:
        return None, None, None, None

    iterations = 0
    error = tolerance + 1
    x = []
    y = []
    while error > tolerance and iterations < max_iterations:
        c = (a + b) / 2
        error = abs(b - a)
        x.append(c)
        y.append(f(c))

        if f(c) == 0:
            error = 0
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
        
        # Convergence condition
        if error <= tolerance:
            break
        # Stop condition
        if iterations >= 2:
            last_error = abs(x[-1] - x[-2])
            if last_error <= tolerance * safety_factor:
                break

    return c, error, iterations, x, y

# Function to calculate the false rule method
def regula_falsi(f, a, b, tolerance=1e-6, max_iterations=100, safety_factor=1.5):
    if f(a) * f(b) > 0:
        return None, None, None, None

    iterations = 0
    error = tolerance + 1
    x = []
    y = []
    while error > tolerance and iterations < max_iterations:
        c = b - ((f(b) * (b - a)) / (f(b) - f(a)))
        error = abs(c - b)
        x.append(c)
        y.append(f(c))

        if f(c) == 0:
            error = 0
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1

        # Convergence condition
        if error <= tolerance:
            break

        # Stop condition
        if iterations >= 2:
            last_error = abs(x[-1] - x[-2])
            if last_error <= tolerance * safety_factor:
                break

    return c, error, iterations, x, y
    
# Function to calculate the root of an equation
def solve_equation(method, f, a, b, tolerance, max_iterations=100):
    if method == "bisection":
        return bisection(f, a, b, tolerance, max_iterations)
    elif method == "regula_falsi":
        return regula_falsi(f, a, b, tolerance, max_iterations)
    else:
        return None, None, None, None
   
# Function to display the app interface
def main():
    st.markdown("<h1 style='text-align: center; color: #218c74;'>Métodos de Bisección y Regula Falsi</h1>", unsafe_allow_html=True)
    st.write("<hr>", unsafe_allow_html=True)
    with st.expander("Instrucciones"):
        st.write("- La ecuación debe ser una función de una variable.")
        st.write("- El intervalo [a, b] debe contener una raíz.")
        st.write("- La tolerancia debe ser un número positivo.")
        st.write("- El número máximo de iteraciones debe ser un número entero positivo.")
        st.write("- El método de bisección solo funciona para funciones continuas.")
        st.write("- El método de falsa posición funciona para funciones continuas y discontinuas.")
        st.write("- El método de falsa posición funciona mejor para funciones con raíces múltiples.")
        st.write("<hr>", unsafe_allow_html=True)
    # Inputs
    method = st.selectbox("Método", ["Bisection", "Regula Falsi"])
    equation_str = st.text_input("Ecuación", "sin(x)", help="Ingrese una ecuación matemática usando la variable x. Puede usar operadores matemáticos como +, -, *, /, y ** para indicar sumas, restas, multiplicaciones, divisiones y potencias respectivamente. También puede utilizar funciones matemáticas comunes como sin(), cos(), tan(), exp(), log(), etc. Recuerde que la función debe estar escrita en términos de la variable x.")
    a = st.number_input("Introduce el valor de a", value=-10.0, step=0.1, help="Límite inferior del intervalo")
    b = st.number_input("Introduce el valor de b", value=10.0, step=0.1, help="Límite superior del intervalo")
    tolerance = st.number_input("Introduce la tolerancia ε", value=1e-6, step=1e-7, help="La tolerancia debe ser un número positivo en notación científica, por ejemplo: 1e-6 para 1x10^-6")
    #max_iterations = st.number_input("Iteraciones máximas", value=100, step=1)
    # Inputs

    # tolerance 
    float_tolerance = float(tolerance)

    # Create button calcular
    if st.button("Calcular"):
        # Create try except equation validation
        try:
            # page header
            st.header("Raiz calculada con : {}".format(method))
            st.write("Encuentra la raíz de la ecuación {} en el intervalo [a, b] usando {} Método.".format(equation_str, method))

            # read equation
            func = read_equation(equation_str)
            
            x = np.linspace(a, b, 1000)
            y = func(x)

        except:
            st.warning("Error: La ecuación no es válida.")
            return

        # Create try except method solve_equation validation
        try:
            # calculate root
            c, error, iterations, x_points, y_points = solve_equation(method.lower().replace(" ", "_"), func, a, b, float_tolerance)    
        except:
            st.warning("Error: El método no pudo converger.")
            return
        
        if c is None:
            st.warning("El método no pudo converger.")
        else:
            st.success("La raíz es {:.6f} con un error de {:.6f}  después {} iteraciones.".format(c, error, iterations))
            '''
            #matplotlib plot
            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.plot(x_points, y_points, 'ro')
            ax.axhline(y=0, color='k')
            ax.axvline(x=c, color='k')
            st.pyplot(fig)
            '''
            # plotly plot
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=y, name="Función"))
            fig.add_trace(go.Scatter(x=x_points, y=y_points, mode="markers", name="iteraciones"))
            # point root
            fig.add_trace(go.Scatter(x=[c], y=[0], mode="markers", name="Raíz"))

            fig.update_layout(title="Función y iteraciones", xaxis_title="x", yaxis_title="y")
            st.plotly_chart(fig)

            # Show iterations table
            expander = st.expander("Ver iteraciones")
            
            #data table iterations,a,b,f(a),f(b),root,f(r),error
            data = {'a': x_points[:-1], 'b': x_points[1:], 'f(a)': y_points[:-1], 'f(b)': y_points[1:], 'Root': x_points[1:], 'f(r)': y_points[1:], 'Error': [np.nan] + [abs(x_points[i] - x_points[i-1]) for i in range(1, iterations)]}

            expander.write("El método utiliza la siguiente fórmula para encontrar la siguiente aproximación:")
            expander.table(pd.DataFrame.from_dict(data, orient='index').transpose())
if __name__ == "__main__":
    main()
