import streamlit as st
from streamlit_option_menu import option_menu
from frontend.fd_display_app_interface_montecarlo import display_app_interface_montecarlo
from frontend.fd_display_app_interface_simpson13 import display_app_interface_simpson13
from frontend.fd_display_app_interface_graficarbise_false import display_app_interface_graficarbise_false
from frontend.fd_display_home_page import display_home_page
from frontend.fd_display_app_interface_m_secante import display_app_interface_m_secante
from frontend.fd_display_app_interface_derivative_calculator import display_app_interface_derivative_calculator
from frontend.fd_display_app_interface_raicesPolinomios import display_app_interface_raicesPolinomios
from frontend.fd_display_app_interface_newton_raphson import display_app_interface_newton_raphson
from frontend.fd_display_app_interface_conversor_bases import display_app_interface_conversor_bases
from frontend.fd_display_app_interface_conversor_bases_ieee754 import display_app_interface_conversor_bases_ieee754
from frontend.fd_display_app_interface_simpson18 import display_app_interface_simpson38
from frontend.fd_display_app_interface_m_rectaguloytrapecio import display_app_interface_rectanguloytrapecio
from frontend.fd_display_app_interface_matrices import display_app_interface_matrices
from frontend.fd_display_app_interface_matrices import display_app_interface_gauss
from frontend.fd_display_app_interface_ajustedecurvas import display_app_interface_ajustesdecurvas
from frontend.fd_display_app_interface_graficador import display_app_interface_graficador

def integracioninterface():
    selected = option_menu(
        menu_title="📈 Metodos de integracion",
        options=["📊 Metodo de simpson 1/3", "📈 Metodo de simpson 3/8","📊 Metodo de rectangulo y trapecio","📊 Metodo de Montecarlo",],
        menu_icon="🧮",
        default_index=1,
        orientation="horizontal",
    )
    if selected == "📊 Metodo de simpson 1/3":
        display_app_interface_simpson13()
    elif selected == "📈 Metodo de simpson 3/8":
        display_app_interface_simpson38()
    elif selected == "📊 Metodo de rectangulo y trapecio":
         display_app_interface_rectanguloytrapecio()
    elif selected == "📊 Metodo de Montecarlo":
        display_app_interface_montecarlo()

def raicesinterface():
    selected = option_menu(
        menu_title="📉 Metodos de raices",
        options=["📉 Método de Bisección y regla falsa","📉 Método de la Secante","📉 Newton Raphson"],
        menu_icon="🧮",
        default_index=1,
        orientation="horizontal",
    )
    if selected =="📉 Método de Bisección y regla falsa":
        display_app_interface_graficarbise_false()
    elif selected == "📉 Método de la Secante":
        display_app_interface_m_secante()
    elif selected == "📉 Newton Raphson":
        display_app_interface_newton_raphson()

def basesinterface():
    selected = option_menu(
        menu_title="🔢 Bases",
        options=["📚 Conversor de Bases", "🖥️ Conversor de Bases IEEE754"
                ],
        icons=["🏠", "🔢","🖥️", ],
        menu_icon="🧮",
        default_index=1,
        orientation="horizontal",
    )
    if selected == "📚 Conversor de Bases":
        display_app_interface_conversor_bases()
    elif selected == "🖥️ Conversor de Bases IEEE754":
        display_app_interface_conversor_bases_ieee754()

def calculointerface():
    selected = option_menu(
        menu_title="🖥️ Cálculo y análisis de funciones",
        options=["📈 Derivadas", "📈 Raices de polinomios", "📊 Ajuste de curvas",
                ],
        menu_icon="🧮",
        default_index=1,
        orientation="horizontal",
    )
    if selected == "📈 Derivadas":
        display_app_interface_derivative_calculator()
    elif selected == "📈 Raices de polinomios":
        display_app_interface_raicesPolinomios()
    elif selected == "📊 Ajuste de curvas":
        display_app_interface_ajustesdecurvas()
def matricesinterface():
    selected = option_menu(
        menu_title="🎲 Matrices",
        options=["⚖️ Operaciones matriciales", "💹 Eliminacion por Gauss Jordan"
                ],
        menu_icon="🧮",
        default_index=1,
        orientation="horizontal",
    )
    if selected == "⚖️ Operaciones matriciales":
        display_app_interface_matrices()
    elif selected == "💹 Eliminacion por Gauss Jordan":
        display_app_interface_gauss()

def display_app_interface_sidebar_menu():
    # Create a sidebar menu
    st.sidebar.title("🧮 Menu Calculadora")
    selected = st.sidebar.selectbox(
        "",
        options=["🏠 Home", "🔢 Bases", "📈 Metodos de integracion","📉 Metodos de raices" ,
                 "🖥️ Cálculo y análisis de funciones","🎲 Matrices","📊 Graficador"],

    )

    # Set page title


    # Display the selected menu item
    if selected == "🏠 Home":
        display_home_page()
    elif selected == "🔢 Bases":
        basesinterface()
    elif selected == "📈 Metodos de integracion":
        integracioninterface()
    elif selected == "📉 Metodos de raices":
        raicesinterface()
    elif selected == "🖥️ Cálculo y análisis de funciones":
        calculointerface()
    elif selected == "🎲 Matrices":
        matricesinterface()
    elif selected == "📊 Graficador":
        display_app_interface_graficador()

# Create a controller displays interface of the app
def display_app_interface():
    # Set page title
    st.set_page_config(page_title="Calcumancia", page_icon=":crystal_ball:", layout="centered")
    # Add sidebar menu
    display_app_interface_sidebar_menu()

# Main function
def main():
    display_app_interface()

if __name__ == "__main__":
    main()
