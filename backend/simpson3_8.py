import streamlit as st
import sympy as sp
from sympy import latex
import numpy as np
import plotly.graph_objects as go


def integrarsimpson38(funcion, intervalo, ndivisiones):
    x = sp.Symbol('x')
    f = sp.lambdify(x, funcion)
    df = sp.diff(funcion, x, 4)
    a = intervalo[0]
    b = intervalo[1]
    if ndivisiones % 3 != 0:
        ndivisiones += 3 - (ndivisiones % 3)
    h = (b - a) / ndivisiones

    resultado = 0
    for i in range(0, ndivisiones-2, 3):
        x0 = a + i*h
        x1 = x0 + h
        x2 = x1 + h
        x3 = x2 + h
        resultado += (3*h/8) * (f(x0) + 3*f(x1) + 3*f(x2) + f(x3))

    error = (b-a) * ((b-a)**4)/(180*(ndivisiones**4)) * abs(df.subs(x, (a+b)/2).evalf())

    integral_latex = f"La integral desde {a} hasta {b} de {funcion} es:"
    error = sp.latex(error)
    resultado = sp.latex(resultado)
    

    return resultado, integral_latex, error



def plot_funcion(funcion, intervalo, n_divisiones):
    x = sp.Symbol('x')
    a, b = intervalo
    h = (intervalo[1] - intervalo[0]) / n_divisiones
    x_values = np.linspace(a, b, num=n_divisiones+1)
    y_values = np.zeros(n_divisiones+1)
    for i in range(n_divisiones+1):
        y_values[i] = funcion.subs(x, x_values[i]).evalf()
    trace = go.Scatter(x=x_values, y=y_values, mode="lines+markers")
    fig = go.Figure(trace)
    fig.update_layout(title="Gráfica de la función", xaxis_title="x", yaxis_title="y")
    fig.update_traces(marker=dict(color=['red', 'blue', 'green', 'yellow', 'purple'] * (n_divisiones//5 + 1)))
    return fig

def main():
    st.markdown("<h1 style='text-align: center; color: #218c74;'>Método de Simpson 3/8</h1>", unsafe_allow_html=True)
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
    funcion = st.text_input("Función:", help=ayuda_funcion)
    
    # Input para el intervalo
    ayuda_intervalo = "Seleccione los límites inferior y superior del intervalo de integración"
    st.write("Ingrese el intervalo de integración:")
    col1, col2 = st.columns(2)
    
    with col1:
        a = st.number_input("Límite inferior", value=-10.0, step=0.1,help=ayuda_intervalo)
        
    with col2:
        b = st.number_input("Límite superior", value=10.0, step=0.1,help=ayuda_intervalo)

    # Input para el número de divisiones
    ayuda_divisiones = "Ingrese el número de divisiones a utilizar. Debe ser un número par."
    n = st.number_input("Número de divisiones (par):", help=ayuda_divisiones, value=10, step=2)
    if st.button("Calcular"):
        
        # Cálculo de la integral y el error
        resultado,integral, error = integrarsimpson38(funcion, [a,b], n)

        # Resultados
        st.write("<hr>", unsafe_allow_html=True)
        st.write("Los resultados obtenidos son los siguientes:")

        col1, col2 = st.columns(2)
        with col1:
            st.write(integral)
            st.latex(rf"\int_{{{a}}}^{{{b}}} {funcion}\, dx")
            st.write("**Resultado:**")
            st.write(resultado)
    
        with col2:
            # Gráfico de la función
            funcion_sym = sp.sympify(funcion)
            fig = plot_funcion(funcion_sym, [a, b], n)
            st.plotly_chart(fig)
            st.write("**Error de estimación:**")
            st.write("{:.6e}".format(float(error)))


