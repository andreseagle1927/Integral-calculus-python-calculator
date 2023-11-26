import streamlit as st
import numpy as np
import plotly.graph_objects as go

def monte_carlo_integration(f, a, b, n):
    x = np.random.uniform(a, b, n)
    fx = f(x)
    integral = np.mean(fx)*(b-a)
    return integral

def plot_function(f, a, b):
    x = np.linspace(a, b, 1000)
    y = f(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name='Función'))
    fig.update_xaxes(title_text='x')
    fig.update_yaxes(title_text='f(x)')
    return fig

def main():
    st.markdown("<h1 style='text-align: center; color: #218c74;'>Método de Montecarlo</h1>", unsafe_allow_html=True)
    st.write("<hr>", unsafe_allow_html=True)
    with st.expander("ℹ️ Para tener en cuenta"):
        st.write("La calculadora de Monte Carlo es una herramienta para aproximar la integral de una función. Para utilizarla, se deben seguir los siguientes pasos:")
        st.write("1. Ingrese la función que desea integrar como un string de Python en el input 'Función'.")
        st.write("2. Ingrese los límites del intervalo de integración en los inputs 'Límite inferior' y 'Límite superior'.")
        st.write("3. Ingrese el número de muestras que desea utilizar para el cálculo de la integral en el input 'Número de muestras'.")
        st.write("4. Haga clic en 'Run' para ejecutar la calculadora y obtener los resultados.")
        st.write("Nota: para obtener una mejor aproximación de la integral, es recomendable utilizar un número grande de muestras.")

    
    # Input para la función
    st.subheader('Función')
    func_str = st.text_input('Función',help='Ingrese la función como un string de Python.')
    func = lambda x: eval(func_str)
    
    # Inputs para los límites del intervalo
    st.subheader('Intervalo')
    a = st.number_input('Límite inferior',value=0,help='Ingrese el límite inferior del intervalo.')
    b = st.number_input('Límite superior',value=1,help='Ingrese el límite superior del intervalo.')
    
    # Input para el número de muestras
    n = st.number_input('Número de muestras',value=10000,help='Ingrese el número de muestras para el cálculo de la integral.')
    n=int(n)
    if st.button("Calcular"):
        try:
            # Cálculo de la integral y graficación de la función
            integral = monte_carlo_integration(func, a, b, n)
            fig = plot_function(func, a, b)
            
            # Resultados
            st.subheader('Resultados')
            st.write('La integral de la función en el intervalo [{}, {}] es:'.format(a, b))
            st.latex(r'\int_{{{}}}^{{{}}} {} dx = {}'.format(a, b, func_str, integral))
            
            # Gráfica
            st.subheader('Gráfica')
            st.plotly_chart(fig)
        except Exception as e:
            st.write("Ocurrió un error al calcular la integral.")
            st.write(e)


if __name__ == '__main__':
    main()