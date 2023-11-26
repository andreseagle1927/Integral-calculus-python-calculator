import numpy as np
import plotly.graph_objs as go
import streamlit as st

def calcular_raices_polinomio(polinomio):
    # List all roots
    roots_all = []
    # List root real 
    root_real = []
    # List root complex
    root_complex = []

    # polinomio = "2 , -7.25 , -5.6 , 25.75 , - 10.85"
    # evaluate the polynomial 
    polinomio = polinomio.replace(" ", "")
    polinomio = polinomio.replace(",", " ")
    polinomio = polinomio.split(" ")
    polinomio = [float(i) for i in polinomio]
    polinomio = np.array(polinomio)
    #print(polinomio)

    # Calculate the roots of the polynomial
    roots = np.roots(polinomio)
    roots_all.append(roots)
    #print(roots)

    # save the roots in a list 
    for i in roots:
        if i.imag == 0:
            #Replace string j by i
            i = str(i).replace("j", "i")
            root_real.append(i)
        else:
            #Replace string j by i
            i = str(i).replace("j", "i")
            root_complex.append(i)

    # Print the roots real
    st.write("Raíces reales:")
    st.write(root_real)

    # Print the roots complex
    st.write("Raíces complejas:")
    st.write(root_complex)  

    # Plot the polynomial
    # Create a list of x values
    x = np.linspace(-10, 10, 1000)
    # Create a list of y values
    y = np.polyval(polinomio, x)
    # Create a trace aditional roots 
    trace_roots = go.Scatter(x=root_real, y=[0]*len(root_real), mode="markers", marker=dict(size=10, color="red"))
    # Create a trace
    trace = go.Scatter(x=x, y=y)
    # Create a layout
    layout = go.Layout(title="Polinomio", xaxis=dict(title="x"), yaxis=dict(title="y"))
    # Create a figure
    fig = go.Figure(data=[trace,trace_roots], layout=layout)
    # Plot and embed in ipython notebook!
    st.plotly_chart(fig, use_container_width=True)

# funcion para main del programa 
def main():
    st.markdown("<h1 style='text-align: center; color: #218c74;'>Raíces de un polinomio</h1>", unsafe_allow_html=True)
    # Ask the user for the function and the value of Xo
    st.write("<hr>", unsafe_allow_html=True)
    with st.expander("ℹ️ Instrucciones"):
        st.write("Esta es una calculadora que te permite calcular las raíces de un polinomio.")
        st.write("Para utilizarla, sigue los siguientes pasos:")
        st.write("1. Ingresa los coeficientes del polinomio separados por coma.")
        st.write("2. Haz clic en 'Calcular' para obtener las raíces del polinomio.")
        st.write("3. El programa te mostrará las raíces reales y complejas del polinomio.")
        st.write("4. También te mostrará una gráfica del polinomio con las raíces reales resaltadas en rojo.")
        st.write("Los coeficientes del polinomio separados por coma (ejemplo: 1,2,3) o (ejemplo: 5.25, -17.4, 0, -10.83, 25.86, -13.25)")

    # Prompt the user to enter the equation in coefficient format
    polinomio = st.text_input("Ingrese los coeficientes del polinomio: ", "2 , -7.25 , -5.6 , 25.75 , - 10.85")
    
    # Create a button to calculate the roots of the polynomial
    if st.button("Calcular"):
        try:
            # result 
            st.write("Resultado:")
            # Print the polynomial
            st.text_input(f"polinomio es:",value=polinomio, key=None, type='default')
            # Calcula las raices del polinomio
            calcular_raices_polinomio(polinomio)
        except:
            st.write("Error: Ingrese los coeficientes correctamente")    

# Ejecuta el programa
if __name__ == "__main__":
    main()            