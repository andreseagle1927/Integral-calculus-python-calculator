import streamlit as st # Import the streamlit library
from backend.ieee754 import decimal_to_bin, decimal_to_hex , bin_to_decimal # Import the decimal_to_bin and decimal_to_hex functions from the ieee754.py file
from frontend.fd_display_app_interface_conversor_bases import is_binario_a_decimal

# Create a function to display the app interface conversor bases format ieee754
def display_app_interface_conversor_bases_ieee754():
    # Add a title
    st.markdown("<h1 style='color: #218c74;'>Conversor Bases IEEE754</h1>", unsafe_allow_html=True)
    
    # Add a subtitle and a text
    
    with st.expander("Instrucciones"):
        st.markdown("""
        Este es un conversor de bases IEEE754. Proporciona las siguientes funcionalidades:
        
        - Conversión de números decimales a precisión simple y doble.
        - Conversión de números en formato estándar a decimal en precisión simple y doble.
        
        **Conversiones de Decimal a IEEE754:**
        
        - En la pestaña "🔴 Simple precisión" puedes ingresar un número decimal y obtener su representación en precisión simple.
        - En la pestaña "🟢 Doble precisión" puedes ingresar un número decimal y obtener su representación en precisión doble.
        
        **Conversiones de IEEE754 a Decimal:**
        
        - En la pestaña "🔵 Estandar precisión simple" puedes ingresar un número en formato estándar de precisión simple y obtener su valor decimal equivalente.
        - En la pestaña "⚪️ Estandar precisión doble" puedes ingresar un número en formato estándar de precisión doble y obtener su valor decimal equivalente.
        
        Para realizar una conversión, ingresa los valores necesarios y presiona el botón "Calcular" correspondiente.
        """)
    # Create tables to display the conversion bases
    tab1, tab2, tab3, tab4 = st.tabs(["🔴 Simple precisión", "🟢 Doble precisión", "🔵 Estandar precisión simple", "⚪️ Estandar precisión doble"])

    with tab1:
        # Add text conversion methot simple precision
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #ffffff;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h1 class="big-font">Conversion Simple Precisión 32bits</h1>', unsafe_allow_html=True)

        # Add a text input
        st.markdown("""
        <style>
        div[class*="stNumberInput"] label {
            font-size: 26px;
            color: #ffffff;
            }
        }
        </style>
        """, unsafe_allow_html=True)

        # Add a text input for decimal
        decimal_input = st.text_input("Ingresar Numero:",value=0, key=4)
        
        # try convert input to float
        try:
            decimal_input_float_simple = float(decimal_input)

            # Create a button convert
            if st.button("Calcular", key=105):
                # Add text result conversion
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
                    color: #ffffff;
                }
                </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="big-font">Resultado Conversion Decimal a Simple Precisión</h1>', unsafe_allow_html=True)
                # conversor bases decimal to simple precision
                (sign, exponent, mantissa, decimal_exponent, decimal_mantissa, decimal_mantissa_str, decimal_equivalent) = decimal_to_bin(decimal_input_float_simple, "simple")
                hex_simple = decimal_to_hex(decimal_input_float_simple, "simple")
                st.text_input(":red[Signo]",value=sign, key="sign1")
                st.text_input(":violet[Exponente]",value=exponent, key="exponent1")
                st.text_input(":orange[Mantissa]",value=mantissa, key="mantissa1")
                st.text_input(":green[Valor decimal equivalente]",value=round(decimal_equivalent,5), key="decimal_equivalent1")
                st.text_input(":green[Estandar]",value="Signo:{"+sign+"}"+"Exponente:{"+exponent +"}"+"Mantissa:{"+mantissa+"}", key="estandar1")
                st.text_input(":green[Cantidad bits]",value=len(sign+exponent+mantissa), key="bits1")
                st.text_input(":green[Hexadecimal]",value=hex_simple, key="hex1")

        except:
            # If input is string and number not convert to float mensaje error
            st.markdown("""
            <style>
            .big-font {
                font-size:20px !important;
                text-align: left;
            }
            </style>
            """, unsafe_allow_html=True)
            st.markdown('<h1 class="big-font">Error: Ingrese un numero decimal, sin caracteres string.</h1>', unsafe_allow_html=True)
            # Reset value input
            decimal_input = 0    

    with tab2:
        # Add text conversion methot double precision
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #ffffff;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h1 class="big-font">Conversion Doble Precisión 64bits</h1>', unsafe_allow_html=True)
        
        # Add a text input
        st.markdown("""
        <style>
        div[class*="stNumberInput"] label {
            font-size: 26px;
            color: #ffffff;
            }
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Add a text input for decimal
        decimal_input = st.text_input("Ingresar Numero:",value=0, key=5)

        # try convert input to float
        try:
            # conversor bases decimal to double precision
            decimal_input_float_doble = float(decimal_input)

            # Create a button convert
            if st.button("Calcular", key=106):
                # Add text result conversion
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
                    color: #ffffff;
                }
                </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="big-font">Resultado Conversion Decimal a Doble Precisión</h1>', unsafe_allow_html=True)
                # conversor bases decimal to double precision
                (sign, exponent, mantissa, decimal_exponent, decimal_mantissa, decimal_mantissa_str, decimal_equivalent) = decimal_to_bin(decimal_input_float_doble, "doble")
                hex_doble = decimal_to_hex(decimal_input_float_doble, "doble")
                st.text_input(":red[Signo]",value=sign, key="sign2")
                st.text_input(":violet[Exponente]",value=exponent, key="exponent2")
                st.text_input(":orange[Mantissa]",value=mantissa, key="mantissa2")
                st.text_input(":green[Valor decimal equivalente]",value=round(decimal_equivalent,5), key="decimal_equivalent2")
                st.text_input(":green[Estandar]",value="Signo:{"+sign+"}"+"Exponente:{"+exponent +"}"+"Mantissa:{"+mantissa+"}", key="estandar2")
                st.text_input(":green[Cantidad bits]",value=len(sign+exponent+mantissa), key="bits2")
                st.text_input(":green[Hexadecimal]",value=hex_doble, key="hex2")

        except:
            # If input is string and number not convert to float mensaje error
            st.markdown("""
            <style>
            .big-font {
                font-size:20px !important;
                text-align: left;
            }
            </style>
            """, unsafe_allow_html=True)
            st.markdown('<h1 class="big-font">Error: Ingrese un numero decimal, sin caracteres string.</h1>', unsafe_allow_html=True)
            # Reset value input
            decimal_input = 0

    with tab3:
        # Add text conversion methot binary to decimal
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #ffffff;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h1 class="big-font">Conversion Estandar a Decimal Presición Simple 32bits:</h1>', unsafe_allow_html=True)

        # Add a text input
        st.markdown("""
        <style>
        div[class*="stNumberInput"] label {
            font-size: 26px;
            color: #ffffff;
            }
        }
        </style>
        """, unsafe_allow_html=True)

        # add form for input binary number simple precision 32bits        
        st.form(key='my_form_32')
        col1, col2 = st.columns(2)
        with col1:
            signo = st.text_input('Signo:', key="signo32")
        with col2:
            exponente = st.text_input('Exponente:', key="exponente32")
        with col1:
            mantissa = st.text_input('Mantissa:', key="mantissa32")

        # Concatenar valores
        binary_input = signo + exponente + mantissa

        # Create a button convert
        if st.button("Calcular", key=107):
            # Verify if input is binaria
            if not is_binario_a_decimal(binary_input):
                # If input is string and number not convert to float mensaje error
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
                }
                </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="big-font">Error: Ingrese un numero Estandar, sin caracteres, 0 y 1 de 32bits.</h1>', unsafe_allow_html=True)
                # Reset value input
                binaria_input = 0
            else:
                # Add text result conversion
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
                    color: #ffffff;
                }
                </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="big-font">Resultado Conversion Estandar a Decimal</h1>', unsafe_allow_html=True)
                (sign, exponent, bin_num, decimal_exponent, mantissa, decimal_mantissa_str, decimal_equivalent) = bin_to_decimal(binary_input, "simple")
                # print result conversion 
                st.text_input(":red[Signo]",value=sign, key="signo32_result")
                st.text_input(":violet[Exponente]",value=exponent, key="exponente32_result")
                st.text_input(":orange[Mantissa]",value=bin_num, key="mantissa32_result")
                st.text_input(":green[Valor decimal equivalente]",value=round(decimal_equivalent,5), key="decimal_equivalent32_result")
                st.text_input(":green[Hexadecimal]",value=decimal_to_hex(decimal_equivalent, "simple"), key="hex32_result")

    with tab4:
        # Add text conversion methot binary to decimal
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            text-align: left;
            color: #ffffff;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h1 class="big-font">Conversion Estandar a Decimal Presición Doble 64bits:</h1>', unsafe_allow_html=True)

        # Add a text input
        st.markdown("""
        <style>
        div[class*="stNumberInput"] label {
            font-size: 26px;
            color: #ffffff;
            }
        }
        </style>
        """, unsafe_allow_html=True)

        # add form for input binary number doble precision 64bits        
        st.form(key='my_form_64')
        col1, col2 = st.columns(2)
        with col1:
            signo = st.text_input('Signo:', key="signo64")
        with col2:
            exponente = st.text_input('Exponente:', key="exponente64")
        with col1:
            mantissa = st.text_input('Mantissa:', key="mantissa64")

        # Concatenar valores
        binary_input = signo + exponente + mantissa

        # Create a button convert
        if st.button("Calcular", key=108):
            # Verify if input is binaria
            if not is_binario_a_decimal(binary_input):
                # If input is string and number not convert to float mensaje error
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
                }
                </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="big-font">Error: Ingrese un numero Estandar, sin caracteres, 0 y 1 de 64bits.</h1>', unsafe_allow_html=True)
                # Reset value input
                binaria_input_doble = 0
            else:
                # Add text result conversion
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    text-align: left;
                    color: #ffffff;
                }
                </style>
                """, unsafe_allow_html=True)
                st.markdown('<h1 class="big-font">Resultado Conversion Estandar a Decimal Doble</h1>', unsafe_allow_html=True)
                (sign, exponent, bin_num, decimal_exponent, mantissa, decimal_mantissa_str, decimal_equivalent) = bin_to_decimal(binary_input, "doble")
                 # print result conversion 
                st.text_input(":red[Signo]",value=sign, key="signo32_result")
                st.text_input(":violet[Exponente]",value=exponent, key="exponente32_result")
                st.text_input(":orange[Mantissa]",value=bin_num, key="mantissa32_result")
                st.text_input(":green[Valor decimal equivalente]",value=round(decimal_equivalent,5), key="decimal_equivalent32_result")
                st.text_input(":green[Hexadecimal]",value=decimal_to_hex(decimal_equivalent, "doble"), key="hex32_result")
                