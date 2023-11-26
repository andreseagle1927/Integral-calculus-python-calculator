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

# Function to calculate the secant method
def secant_method(f, x0, x1, tolerance=1e-6, max_iter=100):
    """
    Encuentra la raíz de la función f usando el método de la secante.
    
    Args:
        f (function): Función a la que se le buscará su raíz.
        x0 (float): Valor inicial para la iteración.
        x1 (float): Otro valor inicial para la iteración.
        tol (float, optional): Tolerancia para la convergencia. Por defecto es 1e-6.
        max_iter (int, optional): Número máximo de iteraciones. Por defecto es 100.
        
    Returns:
        float: Aproximación de la raíz de la función f.
    """
    iteraciones = []
    i = 0
    while i < max_iter:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        error = abs(x2 - x1)
        iteraciones.append({"x0": x0, "x1": x1, "raiz": x2, "error": error})
        if error < tolerance:
            return x2, iteraciones
        x0 = x1
        x1 = x2
        i += 1
    raise ValueError("La función no converge.")

def main():
    # Title
    st.markdown("<h1 style='text-align: center; color: #218c74;'>Método de la Secante</h1>", unsafe_allow_html=True)
    st.write("<hr>", unsafe_allow_html=True)
    with st.expander("Instrucciones"):
        st.markdown("""
        Esta es una calculadora del Método de la Secante. Proporciona las siguientes funcionalidades:

        - Ingrese una ecuación matemática utilizando la variable `x`. Puede utilizar operadores matemáticos como `+`, `-`, `*`, `/` y `**` para indicar sumas, restas, multiplicaciones, divisiones y potencias respectivamente. También puede utilizar funciones matemáticas comunes como `sin()`, `cos()`, `tan()`, `exp()`, `log()`, etc. Asegúrese de que la función esté escrita en términos de la variable `x`.
        - Ingrese los valores iniciales `x0` y `x1`.
        - Ingrese una tolerancia para la convergencia del método.
        - Presione el botón "Calcular" para obtener la raíz de la función utilizando el Método de la Secante.

        **Instrucciones de uso:**

        1. Ingrese una ecuación matemática en el campo "Ecuación". Por ejemplo, puede ingresar `exp(-0.5*x) + 3.5*log(x) - 5.25`.
        2. Ingrese los valores iniciales `x0` y `x1` en los campos correspondientes.
        3. Ingrese una tolerancia en el campo "Tolerancia".
        4. Presione el botón "Calcular".
        5. Se mostrará la raíz aproximada y la cantidad de iteraciones realizadas.
        6. También se mostrará una gráfica de la función `f(x)` y la aproximación de la raíz.

        **Nota:** Asegúrese de que la función sea continua y tenga una raíz en el intervalo definido por los valores iniciales `x0` y `x1`.

        """)
    # Input equation
    equation_str = st.text_input("Ecuación", "exp(-0.5*x) + 3.5*log(x) - 5.25", help="Ingrese una ecuación matemática usando la variable x. Puede usar operadores matemáticos como +, -, *, /, y ** para indicar sumas, restas, multiplicaciones, divisiones y potencias respectivamente. También puede utilizar funciones matemáticas comunes como sin(), cos(), tan(), exp(), log(), etc. Recuerde que la función debe estar escrita en términos de la variable x.")
    # Input initial values
    x0 = st.number_input("Valor inicial x0", value=1.0 , help="Límite inferior del intervalo")
    # Input initial values
    x1 = st.number_input("Valor inicial x1", value=3.0, help="Límite superior del intervalo")
    # Input tolerance
    tolerance = st.text_input("Tolerancia", "0.0001")
    # Input max iterations
    # max_iter = st.number_input("Número máximo de iteraciones", 100)
    
    # Convert tolerance to float
    tolerance = float(tolerance)

    # Read equation
    f = read_equation(equation_str)

    # Create button to calculate the root
    if st.button("Calcular"):

        # Create try except to catch errors
        try:
            # Calculate root approximation
            raiz,iteraciones= secant_method(f, x0, x1, tolerance)

            # Print success message
            st.success("La raíz es {} después {} iteraciones.".format(raiz, len(iteraciones)))
        except:
            # Print error message
            st.warning("Error: Defina correctamente los datos a evaluar.")
            return

        # Create table with iterations
        columnas = ["Iteración", "x0", "x1", "raiz", "f(raiz)", "error"]
        datos = []
        for i, iteracion in enumerate(iteraciones):
            datos.append([i+1, iteracion["x0"], iteracion["x1"], iteracion["raiz"], f(iteracion["raiz"]), abs(iteracion["error"])])
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
        fig.add_trace(go.Scatter(x=[raiz], y=[f(raiz)], mode="markers", marker=dict(color="red"), name="Aproximación de la raíz"))
        fig.update_layout(title="Gráfica de la función f(x) y su aproximación de la raíz", xaxis_title="x", yaxis_title="f(x)")

        # Show plot
        st.plotly_chart(fig)

        #expander
        expander = st.expander("Tabla de iteraciones")
            
        # Show table
        expander.table(tabla_df)

    
# Run main function
if __name__ == "__main__":
    main()   