
import streamlit as st # Import the streamlit library
from backend.conversor_bases import convert # Import the convert function from the conversor_bases.py file

# function verification if input is binaria decimal to binaria
def is_binario_a_decimal(binaria_input):
    if all(char in "01." for char in binaria_input):
        binaria_input = binaria_input.replace(".", "")
        try:
            decimal = int(binaria_input, 2)
            return decimal
        except ValueError:
            return False
    return False


# Function verify if input is octal
def is_octal(octal_input):
    # Verify if input is octal and decimal octal
    if all(char in "01234567." for char in octal_input):
        octal_input = octal_input.replace(".", "")
        try:
           decimal = int(octal_input, 8)
           return decimal
        except ValueError:
           return False
    return False

# function verification if input is hexadecimal and decimal hexadecimal
def is_hexadecimal(hexadecimal_input):
    # Verify if input is hexadecimal and decimal hexadecimal
    if all(char in "0123456789ABCDEFabcdef." for char in hexadecimal_input):
        hexadecimal_input = hexadecimal_input.replace(".", "")
        try:
            decimal = int(hexadecimal_input, 16)
            return decimal
        except ValueError:
            return False
    return False

# Create a function to display the app interface conversor bases
def display_app_interface_conversor_bases():
    # Add a title
    st.markdown("<h1 style='color: #218c74;'>Conversor de bases</h1>", unsafe_allow_html=True)
    with st.expander("ℹ️ Instrucciones"):
        st.write("Esta es una calculadora de conversión de bases numéricas.")
        st.write("Puedes utilizarla para convertir números entre las siguientes bases: decimal, octal, hexadecimal y binario.")
        st.write("Para utilizarla, sigue los siguientes pasos:")
        st.write("1. Selecciona la pestaña correspondiente a la base de origen del número que deseas convertir.")
        st.write("2. Ingresa el número en el campo de texto proporcionado.")
        st.write("   - Asegúrate de ingresar el número en el formato correcto para la base seleccionada.")
        st.write("   - Por ejemplo, para binario, solo se permiten los caracteres '0' y '1'.")
        st.write("3. Haz clic en el botón 'Calcular' para realizar la conversión.")
        st.write("4. Se mostrarán los resultados de la conversión en las pestañas correspondientes a las bases de destino.")
        st.write("   - Los resultados se actualizarán automáticamente cuando cambies el número de entrada.")

    # Add a subtitle and a text
    # Create tables to display the conversion bases
    tab1, tab2, tab3, tab4= st.tabs(["🔴 Decimal", "🟢 Octal", "🔵 Hexadecimal", "⚪️ Binario"])

    with tab1:
        # Add text conversion method
        st.markdown("""
        
        """, unsafe_allow_html=True)
        st.write("Esta sección permite convertir un número decimal a otras bases numéricas.")
        

        decimal_input = st.text_input("Ingresar Numero:", value=0, key=0)
        # If input is string and number not convert to float
        try:
            # Convert input to float
            decimal_input_float = float(decimal_input)

            # Create a button conversion
            if st.button("Calcular", key= 101):
                # Add text result conversion
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
                    color: white              
                }
                </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="big-font">Resultado Conversion Decimal todas las bases</h1>', unsafe_allow_html=True)
                # conversor bases decimal
                st.text_input(":green[Resultado decimal a binario]:", value=convert(decimal_input_float,'decimal','binary'), key="result_binary_1")
                st.text_input(":green[Resultado decimal a octal:]", value=convert(decimal_input_float,'decimal','octal'), key="result_octal_1")
                st.text_input(":green[Resultado decimal a hexadecimal:]", value=convert(decimal_input_float,'decimal','hexadecimal'), key="result_hexadecimal_1")
        except:
            # If input is string and number not convert to float error message
            st.markdown("""
            <style>
            .big-font {
                font-size:20px !important;
                text-align: left;
                color: white      
            }
            </style>
            """, unsafe_allow_html=True)
            st.markdown('<h1 class="big-font">Error: Ingrese un número decimal o entero, sin caracteres string.</h1>', unsafe_allow_html=True)
            # Reset value input
            decimal_input_float = 0


    with tab2:
        # Add text conversion methot
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #white;
        }
        </style>
        """, unsafe_allow_html=True)
        st.write("Esta sección permite convertir un número octal a otras bases numéricas.")

        # Add a text input
        st.markdown("""
        <style>
        div[class*="stNumberInput"] label {
            font-size: 26px;
            color: #000000;
            }
        }
        </style>
        """, unsafe_allow_html=True)

        # Add a text input for Octal
        octal_input = st.text_input("Ingresar Numero:", value=0 ,key=1)
        
        # Create a button conversion
        if st.button("Calcular" , key=105):
            # If input is number convert octal
            if is_octal(octal_input):
                # Add text result conversion
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
                    color: #white;
                }
                </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="big-font">Resultado Conversion Octal todas las bases</h1>', unsafe_allow_html=True)
                # conversor bases octal
                st.text_input(":green[Resultado octal a decimal]:", value=convert(octal_input,'octal','decimal'), key="result_decimal_1")
                st.text_input(":green[Resultado octal a binario:]", value=convert(octal_input,'octal','binary'), key="result_binary_2")
                st.text_input(":green[Resultado octal a hexadecimal:]", value=convert(octal_input,'octal','hexadecimal'), key="result_hexadecimal_2")


    with tab3:
        # Add text conversion methot
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #white;
        }
        </style>
        """, unsafe_allow_html=True)
        st.write("Esta sección permite convertir un número hexadecimal a otras bases numéricas.")

        # Add a text input
        st.markdown("""
        <style>
        div[class*="stNumberInput"] label {
            font-size: 26px;
            color: #000000;
            }
        }
        </style>
        """, unsafe_allow_html=True)

        # Add a text input for hexadecimal
        hexadecimal_input = st.text_input("Ingresar Numero:", value=0 ,key=2)

        # Create a button conversion
        if st.button("Calcular" , key=103):
            # Verify if input is hexadecimal
            if not is_hexadecimal(hexadecimal_input):
                # If input is string and number not convert to float mensaje error
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
        white          </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="big-font">Error: Ingrese un numero hexadecimal valido.</h1>', unsafe_allow_html=True)
                # Reset value input
                hexadecimal_input = 0
            else:
                # Add text result conversion
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
                    color: #white;
                }
                </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="big-font">Resultado Conversion Hexadecimal todas las bases</h1>', unsafe_allow_html=True)
                # conversor bases hexadecimal
                st.text_input(":green[Resultado hexadecimal a decimal]:", value=convert(hexadecimal_input,'hexadecimal','decimal'), key="result_decimal_2")
                st.text_input(":green[Resultado hexadecimal a octal]:", value=convert(hexadecimal_input,'hexadecimal','octal'), key="result_octal_2")
                st.text_input(":green[Resultado hexadecimal a binario]:", value=convert(hexadecimal_input,'hexadecimal','binary'), key="result_binary_3")

    with tab4:
        # Add text conversion methot
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #white;
        }
        </style>
        """, unsafe_allow_html=True)
        st.write("Esta sección permite convertir un número Binario a otras bases numéricas.")

        # Add a text input
        st.markdown("""
        <style>
        div[class*="stNumberInput"] label {
            font-size: 26px;
            color: #000000;
            }
        }
        </style>
        """, unsafe_allow_html=True)

        # Add a text input for binaria
        binaria_input = st.text_input("Ingresar Numero:",value=0, key=3)

        # Create a button conversion
        if st.button("Calcular" , key=104):
            # Verify if input is binaria
            if not is_binario_a_decimal(binaria_input):
                # If input is string and number not convert to float mensaje error
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
        white          </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="big-font">Error: Ingrese un numero estandar, sin caracteres 0 y 1.</h1>', unsafe_allow_html=True)
                # Reset value input
                binaria_input = 0
            else:
                # Add text result conversion
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
                    color: #white;
                }
                </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="big-font">Resultado Conversion Binaria todas las bases</h1>', unsafe_allow_html=True)
                # conversor bases binaria
                st.text_input(":green[Resultado binario a decimal]:", value=convert(binaria_input,'binary','decimal'), key="result_decimal_3")
                st.text_input(":green[Resultado binario a octal]:", value=convert(binaria_input,'binary','octal'), key="result_octal_3")
                st.text_input(":green[Resultado binario a hexadecimal]:", value=convert(binaria_input,'binary','hexadecimal'), key="result_hexadecimal_3")