import streamlit as st
import plotly.graph_objects as go
import numpy as np

def rectangle_left(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    area = h * sum(y[:-1])
    return area

def rectangle_right(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    area = h * sum(y[1:])
    return area

def rectangle_midpoint(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a + h/2, b - h/2, n)
    y = f(x)
    area = h * sum(y)
    return area

def trapezoid(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    area = h * (sum(y) - (y[0] + y[-1])/2)
    return area

def integrate(f, a, b, n, method):
    if method == "Rectangle - Left":
        area = rectangle_left(f, a, b, n)
    elif method == "Rectangle - Right":
        area = rectangle_right(f, a, b, n)
    elif method == "Rectangle - Midpoint":
        area = rectangle_midpoint(f, a, b, n)
    elif method == "Trapezoid":
        area = trapezoid(f, a, b, n)
    else:
        area = 0
    return area

def plot_function(f, a, b):
    x = np.linspace(a, b, 1000)
    y = eval(f)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name="Función a Integrar", line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=[a, b], y=[0, 0], mode="markers", name="Puntos de Integración", marker=dict(color=["red", "green"], size=10)))
    fig.update_layout(title="Gráfica de la Función a Integrar", xaxis_title="x", yaxis_title="y")
    return fig

def main():
    st.markdown("<h1 style='text-align: center; color: #218c74;'>Método de Rectangulo y Trapecio 1/3</h1>", unsafe_allow_html=True)
    with st.expander("ℹ️ Para tener en cuenta"):
        st.write("El método de Rectángulo o Trapecio  es una técnica para aproximar la integral de una función. Para utilizarlo, se deben seguir los siguientes pasos:")
        st.write("1. Seleccionar una función a integrar y un intervalo.")
        st.write("2. Elegir un número de divisiones.")
        st.write("3. Elegir el método de integración (Rectángulo o Trapecio).")
        st.write("4. Calcular la integral y el error asociado.")
    ayuda_metodo = "Seleccione el método de integración a utilizar (Rectángulo o Trapecio)."
    method = st.selectbox("Selecciona el método de integración: ", ["Rectangle ", "Trapezoid"], help=ayuda_metodo)
        
    # Ayudas
    ayuda_funcion = "Ingrese la función matemática que desea integrar, utilizando la sintaxis de Python y SymPy."
    ayuda_intervalo = "Seleccione los límites inferior y superior del intervalo de integración."
    ayuda_divisiones = "Seleccione el número de divisiones para aproximar la integral. A mayor número de divisiones, mayor será la precisión de la aproximación."
    # Input para el método de integración
    func = st.text_input("Introduce la función a integrar: ", value="x**2", help=ayuda_funcion)
    a = st.number_input("Introduce el límite inferior de la integral: ", value=0.0, help=ayuda_intervalo)
    b = st.number_input("Introduce el límite superior de la integral: ", value=1.0, help=ayuda_intervalo)
    n = st.number_input("Introduce el número de puntos: ", value=10, step=1, help= ayuda_divisiones)

    if st.button("Calcular"):
        
        try:
            if method.startswith("Rectangle"):
                left_end_point = integrate(lambda x: eval(func), a, b, int(n), "Rectangle - Left")
                right_end_point = integrate(lambda x: eval(func), a, b, int(n), "Rectangle - Right")
                midpoint = integrate(lambda x: eval(func), a, b, int(n), "Rectangle - Midpoint")
                col1, col2 = st.columns(2)
                with col1:
                    st.latex(fr"Punto inicio: {left_end_point:.2f}")
                    st.latex(fr"Punto medio: {midpoint:.2f}")
                    st.latex(fr"Punto final: {right_end_point:.2f}")

                with col2:
                    fig = plot_function(func, a, b)
                    st.plotly_chart(fig)
            else:
                col1, col2 = st.columns(2)
                with col1:
                    result = integrate(lambda x: eval(func), a, b, int(n), method)
                    st.latex(fr"Resultado : {result:.2f}")

                with col2:
                    fig = plot_function(func, a, b)
                    st.plotly_chart(fig)
        except Exception as e:
            st.write("Ocurrió un error al calcular la integral.")
            st.write(e)





if __name__ == "__main__":
    main()