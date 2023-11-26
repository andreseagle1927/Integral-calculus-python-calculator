
import streamlit as st
import sympy as sp
from sympy import latex
import numpy as np
import plotly.graph_objects as go
from scipy.integrate import quad


def integrar(funcion, intervalo, n_divisiones):
    x = sp.Symbol('x')
    f = sp.lambdify(x, funcion)

    # Calcula la integral numéricamente utilizando quad()
    resultado, error = quad(f, intervalo[0], intervalo[1])

    integral_latex = f"La integral desde {intervalo[0]} hasta {intervalo[1]} de {funcion} es:"
    error_latex = latex(error)

    return resultado, integral_latex, error_latex


def plot_funcion(funcion, intervalo, n_divisiones):
    x = sp.Symbol('x')
    a, b = intervalo
    h = (b - a) / n_divisiones
    x_values = np.linspace(a, b, num=n_divisiones + 1)
    y_values = np.zeros(n_divisiones + 1)
    for i in range(n_divisiones + 1):
        y_values[i] = funcion.subs(x, x_values[i]).evalf()
    trace = go.Scatter(x=x_values, y=y_values, mode="lines+markers")
    fig = go.Figure(trace)
    fig.update_layout(title="Gráfica de la función", xaxis_title="x", yaxis_title="y")
    fig.update_traces(marker=dict(color=['red', 'blue', 'green', 'yellow', 'purple'] * (n_divisiones // 5 + 1)))
    return fig


def main():
    st.markdown("<h1 style='text-align: center; color: #218c74;'>Método de Simpson 1/3</h1>", unsafe_allow_html=True)
    st.write("<hr>", unsafe_allow_html=True)
    st.write("Este programa calcula la integral de una función en un intervalo dado utilizando el método de Simpson 1/3.")

    # Expander para información del método
    with st.expander("ℹ️ Para tener en cuenta"):
        st.write("El método de Simpson 1/3 es una técnica para aproximar la integral de una función. Para utilizarlo, se deben seguir los siguientes pasos:")
        st.write("1. Seleccionar una función a integrar y un intervalo.")
        st.write("2. Elegir un número de divisiones que sea par.")
        st.write("3. Calcular la integral y el error asociado.")

    # Input para la función
    ayuda_funcion = "Ingrese la función matemática que desea integrar, utilizando la sintaxis de Python y SymPy."
    funcion = st.text_input("Función:", value="sqrt(x) * exp(- (x/10)**2)", help=ayuda_funcion)

    # Input para el intervalo
    ayuda_intervalo = "Ingrese los límites inferior y superior del intervalo de integración."
    intervalo_inicio = st.number_input("Límite inferior del intervalo:", value=0.0, step=0.1, format="%.8f", help=ayuda_intervalo)
    intervalo_fin = st.number_input("Límite superior del intervalo:", value=10.0, step=0.1, format="%.8f", help=ayuda_intervalo)
    intervalo = [intervalo_inicio, intervalo_fin]

    # Input para el número de divisiones
    ayuda_divisiones = "Seleccione un número par de divisiones para aproximar la integral. A mayor número de divisiones, mayor será la precisión de la aproximación."
    n_divisiones = st.slider("Seleccione el número de divisiones:", value=10, step=2, min_value=2, max_value=500, help=ayuda_divisiones)

    if st.button("Calcular"):
        try:
            x = sp.symbols('x')
            funcion_expr = sp.sympify(funcion)
            resultado, integral_latex, error_latex = integrar(funcion_expr, intervalo, n_divisiones)
            st.write(f"{integral_latex}")
            st.latex(rf"\int_{{{intervalo[0]}}}^{{{intervalo[1]}}} {latex(funcion_expr)}\, dx")
            fig = plot_funcion(funcion_expr, intervalo, n_divisiones)
            st.plotly_chart(fig)
            st.write(f"El valor de la integral es: {resultado:.8f}")
            st.write(f"El error estimado es: {error_latex}")
        except Exception as e:
            st.write("Ocurrió un error al calcular la integral.")
            st.write(e)


if __name__ == "__main__":
    main()


"""
import streamlit as st
import sympy as sp
from sympy import latex
import numpy as np
import plotly.graph_objects as go
from scipy.integrate import quad


def integrar(funcion, intervalo, n_divisiones):
    x = sp.Symbol('x')
    f = sp.lambdify(x, funcion)

    # Calcula la integral numéricamente utilizando quad()
    resultado, error = quad(f, intervalo[0], intervalo[1])

    integral_latex = f"La integral desde {intervalo[0]} hasta {intervalo[1]} de {funcion} es:"
    error_latex = latex(error)

    return resultado, integral_latex, error_latex


def plot_funcion(funcion, intervalo, n_divisiones):
    x = sp.Symbol('x')
    a, b = intervalo
    h = (b - a) / n_divisiones
    x_values = np.linspace(a, b, num=n_divisiones + 1)
    y_values = np.zeros(n_divisiones + 1)
    for i in range(n_divisiones + 1):
        y_values[i] = funcion.subs(x, x_values[i]).evalf()
    trace = go.Scatter(x=x_values, y=y_values, mode="lines+markers")
    fig = go.Figure(trace)
    fig.update_layout(title="Gráfica de la función", xaxis_title="x", yaxis_title="y")
    fig.update_traces(marker=dict(color=['red', 'blue', 'green', 'yellow', 'purple'] * (n_divisiones // 5 + 1)))
    return fig


def main():
    st.markdown("<h1 style='text-align: center; color: #218c74;'>Método de Simpson 1/3</h1>", unsafe_allow_html=True)
    st.write("<hr>", unsafe_allow_html=True)
    st.write("Este programa calcula la integral de una función en un intervalo dado utilizando el método de Simpson 1/3.")

    # Expander para información del método
    with st.expander("ℹ️ Para tener en cuenta"):
        st.write("El método de Simpson 1/3 es una técnica para aproximar la integral de una función. Para utilizarlo, se deben seguir los siguientes pasos:")
        st.write("1. Seleccionar una función a integrar y un intervalo.")
        st.write("2. Elegir un número de divisiones que sea par.")
        st.write("3. Calcular la integral y el error asociado.")

    # Input para la función
    ayuda_funcion = "Ingrese la función matemática que desea integrar, utilizando la sintaxis de Python y SymPy."
    funcion = st.text_input("Función:", value="sqrt(x) * exp(- (x/10)**2)", help=ayuda_funcion)

    # Input para el intervalo
    ayuda_intervalo = "Ingrese los límites inferior y superior del intervalo de integración."
    intervalo_inicio = st.number_input("Límite inferior del intervalo:", value=0.0, step=0.1, format="%.8f", help=ayuda_intervalo)
    intervalo_fin = st.number_input("Límite superior del intervalo:", value=np.inf, step=0.1, format="%.8f", help=ayuda_intervalo)
    intervalo = [intervalo_inicio, intervalo_fin]

    # Input para el número de divisiones
    ayuda_divisiones = "Seleccione un número par de divisiones para aproximar la integral. A mayor número de divisiones, mayor será la precisión de la aproximación."
    n_divisiones = st.slider("Seleccione el número de divisiones:", value=10, step=2, min_value=2, max_value=500, help=ayuda_divisiones)
    if st.button("Calcular"):
        try:
            resultado, integral_latex, error_latex = integrar(funcion, intervalo, n_divisiones)
            st.write(f"{integral_latex} ")
            st.latex(rf"\int_{{{intervalo[0]}}}^{{{intervalo[1]}}} {funcion}\, dx")
            fig = plot_funcion(sp.sympify(funcion), intervalo, n_divisiones)
            st.plotly_chart(fig)
            st.write(f"El valor de la integral es: {resultado:.8f}")
            st.write(f"El error estimado es: {error_latex}")
        except Exception as e:
            st.write("Ocurrió un error al calcular la integral.")
            st.write(e)


if __name__ == "__main__":
    main()
"""