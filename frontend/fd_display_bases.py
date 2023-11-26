import streamlit as st

# Establecemos la configuración de la página para colocar la barra lateral en el lado izquierdo


from frontend.fd_display_app_interface_conversor_bases import display_app_interface_conversor_bases
from frontend.fd_display_app_interface_conversor_bases_ieee754 import display_app_interface_conversor_bases_ieee754

from streamlit_option_menu import option_menu

def fd_display_bases():
    # Agregamos los botones a la sidebar
    with st.sidebar:
        st.write("Elige calculadora:")
        conv_bases = st.button("Conversor de Bases", key="conv_bases")
        conv_ieee = st.button("Conversor de Bases IEEE754", key="conv_ieee")

    # Dependiendo de la opción seleccionada, mostramos la interfaz correspondiente
    if conv_bases:
        display_app_interface_conversor_bases()
    elif conv_ieee:
        display_app_interface_conversor_bases_ieee754()



