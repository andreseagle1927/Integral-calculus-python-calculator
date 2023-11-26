import streamlit as st
import sympy as sp
import plotly.graph_objects as go
import numpy as np

# function to calculate the derivates 2
def verificar_entrada_usuario(funcion):
    # Verificar si la entrada es una cadena
    if not isinstance(funcion, str):
        raise TypeError("La entrada debe ser una cadena de caracteres.")

    # Verificar si la entrada es una ecuación válida
    try:
        # Define la variable simbólica x
        x = sp.symbols('x')
        # Convertir la entrada a una expresión sympy
        expresion = sp.sympify(funcion)
        # Evaluar la expresión en el punto x=0
        valor_evaluado = expresion.subs(x, 0)
    except Exception as e:
        error_type = type(e).__name__
        error_msg = str(e)
        raise ValueError(
            f"La entrada no es una ecuación matemática válida. {error_type}: {error_msg}")

    # Verificar si la expresión contiene la variable x
    if x not in expresion.free_symbols:
        raise ValueError("La entrada debe contener la variable x.")

    # La entrada es válida
    return True


def calcular_derivadas2(funcion, n=1, xO=2.5):
    # try to convert the function to a sympy function
    try:
        # Define la variable simbólica x
        x = sp.symbols('x')
        # Calcular la derivada n veces
        derivada = funcion
        for i in range(n):
            derivada = sp.diff(derivada, x)

        # Simplificar la derivada
        derivada_simplificada = sp.simplify(derivada)

        # Evaluar la derivada en un punto
        valor_derivada = derivada_simplificada.subs(x, xO)

        # Save the results in a dictionary
        resultados = {
            'funcion': funcion,
            'derivada0': derivada,
            'derivada': derivada_simplificada,
            'valor_derivada': valor_derivada,
            'x': x
        }

        # Return the results
        return resultados
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
    st.markdown("<h1 style='text-align: center; color: #218c74;'>Calculadora de Derivadas</h1>", unsafe_allow_html=True)
    # Ask the user for the function and the value of Xo
    st.write("<hr>", unsafe_allow_html=True)
    with st.expander("ℹ️ Para tener en cuenta"):
        st.write("Esta es una calculadora que te permite calcular la derivada de una función utilizando la definición matemática de la derivada.")
        st.write("Para utilizarla, sigue los siguientes pasos:")
        st.write("1. Selecciona la función que deseas derivar.")
        st.write("2. Selecciona el valor de x donde deseas calcular la derivada.")
        st.write("3. Selecciona el numero de derivadas a calcular.")
        st.write("4. Haz clic en 'Calcular' para obtener la derivada de la función en el punto seleccionado.")

    funcion = st.text_input("Introduce la función:", value="((sin(x)+pi)/(sin(x)-pi))-pi*sin(x)", help="Ingrese una ecuación matemática usando la variable x. Puede usar operadores matemáticos como +, -, *, /, y ** para indicar sumas, restas, multiplicaciones, divisiones y potencias respectivamente. También puede utilizar funciones matemáticas comunes como sin(), cos(), tan(), exp(), log(), etc. Recuerde que la función debe estar escrita en términos de la variable x.")
    xO = st.number_input("Introduce el valor de Xo:", value=0.0)

    # Ask the user for the number of derivatives to calculate
    n = st.slider("Número de derivadas a calcular:",
                  min_value=1, max_value=10, value=1, step=1)

    # Calculate the derivatives
    resultados = calcular_derivadas2(funcion, n, xO)

    if st.button("Calcular"):
        # Show the results in LaTeX
        st.latex(r"\text{La función original es: } f(x) = " +
                 sp.latex(resultados['funcion']))
        st.latex(r"\text{La primera derivada sin simplificar es: } f^{(1)}(x) = " +
                 sp.latex(resultados['derivada0']))
        st.latex(r"\text{La primera derivada simplificada es: } f^{(1)}(x) = " +
                 sp.latex(resultados['derivada']))
        st.latex(r"\text{El valor de la primera derivada en } xO=2.5 \text{ es: } f^{(1)}(" +
                 str(resultados['x']) + r") = " + sp.latex(resultados['valor_derivada']))

        # Define los valores de x para graficar
        x_vals = np.linspace(-10, 10, 200)

        # Evalúa la derivada en los valores de x
        derivada_vals = [float(resultados['derivada'].subs(
            resultados['x'], x_val)) for x_val in x_vals]

        # Crea la figura
        fig = go.Figure()

        # Agrega la curva de la derivada a la figura
        fig.add_trace(go.Scatter(x=x_vals, y=derivada_vals, mode='lines'))

        # Agrega un título y etiquetas para los ejes
        fig.update_layout(title="Gráfica de la derivada",
                          xaxis_title="x", yaxis_title="f'(x)")

        # Muestra la figura
        st.plotly_chart(fig)


# Run main function
if __name__ == "__main__":
    main()
