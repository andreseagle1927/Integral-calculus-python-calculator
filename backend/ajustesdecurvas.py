import streamlit as st
import numpy as np
import plotly.graph_objects as go

class Ajuste:
    def __init__(self, filax=None, filay=None):
        self.x = np.array(filax) if filax is not None else None
        self.y = np.array(filay) if filay is not None else None

    def getGrados(self):
        if self.x is None:
            return 0
        grados = len(set(self.x))
        return min(grados, 7)

    def curveFit(self):
        nCopy = self.getGrados()
        A = self.x[:, np.newaxis] ** nCopy
        nCopy -= 1
        while nCopy >= 1:
            A = np.append(A, self.x[:, np.newaxis] ** nCopy, axis=1)
            nCopy -= 1
        A = np.column_stack((A, np.ones_like(self.x)))
        AT = np.transpose(A)
        S = np.dot(AT, A)
        z = np.dot(AT, self.y[:, np.newaxis])
        SInv = np.linalg.inv(S)
        sol = np.dot(SInv, z)
        return sol.flatten()
def plotly_graph(x, y, coeficientes):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Datos'))

    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = np.polyval(coeficientes[::-1], x_fit)
    fig.add_trace(go.Scatter(x=x_fit, y=y_fit, mode='lines', name='Ajuste de curva'))

    fig.update_layout(title='Ajuste de curva con mínimos cuadrados',
                      xaxis_title='x',
                      yaxis_title='y')

    st.plotly_chart(fig)

def main():

    st.markdown("<h1 style='text-align: center; color: #218c74;'>Ajuste de curva con mínimos cuadrados</h1>", unsafe_allow_html=True)
    st.write("<hr>", unsafe_allow_html=True)
    with st.expander("ℹ️ Instrucciones"):
        st.write("Esta es una calculadora que te permite realizar un ajuste de curva utilizando el método de mínimos cuadrados.")
        st.write("Para utilizarla, sigue los siguientes pasos:")
        st.write("1. Ajusta el número de puntos utilizando el control deslizante.")
        st.write("2. Ingresa las coordenadas de los puntos en las columnas correspondientes.")
        st.write("3. Haz clic en 'Calcular' para obtener el ajuste de curva.")
        st.write("4. Los coeficientes del ajuste y el gráfico resultante se mostrarán a continuación.")

    # Obtener el número de puntos
    num_puntos = st.slider("Número de puntos", min_value=2, max_value=12, value=5)

    # Inicializar las listas de coordenadas
    x_coords = []
    y_coords = []

    # Recopilar las coordenadas de los puntos
    st.subheader("Ingresar coordenadas de los puntos:")

    col1, col2 = st.columns(2)  # Creamos dos columnas

    for i in range(num_puntos):
        with col1:
            x = st.number_input(f"x{i+1}", key=f"x{i+1}")
            x_coords.append(x)

        with col2:
            y = st.number_input(f"y{i+1}", key=f"y{i+1}")
            y_coords.append(y)

    # Verificar que se hayan ingresado al menos dos puntos
    if len(x_coords) < 2:
        st.error("Se deben ingresar al menos dos puntos.")
        return

    if st.button("Calcular"):
        # Calcular los coeficientes de ajuste
        try:
            ajuste = Ajuste(x_coords, y_coords)
            coeficientes = ajuste.curveFit()

            # Mostrar los coeficientes para cada grado
            st.subheader("Ajuste por grados:")
            for grado, coeficiente in enumerate(coeficientes[::-1]):
                st.latex(f"Grado {grado+1}: {coeficiente}")

            # Generar el gráfico
            plotly_graph(x_coords, y_coords, coeficientes)

        except Exception as e:
            st.error("Ocurrió un error durante el cálculo.")

if __name__ == "__main__":
    main()

