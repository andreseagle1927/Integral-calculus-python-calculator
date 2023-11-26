import streamlit as st

def display_home_page():
    # Set page width and height
    page_width = 800
    page_height = 500

    # Set page background color and padding
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #2c3e50;
            padding: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Set page layout using columns
    col1, col2 = st.columns([5,3 ])
    
    # Add logo to left column
    with col1:
        st.image("./images/Logohome.jpg", width=400)

    # Add title to right column
    with col2:
        st.markdown(
            """
            <style>
            .big-font {
                font-size: 5rem;
                text-align: right;
                color: #218c74;
                margin-top: 4rem;
                font-family: sans-serif;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown('<h1 class="big-font">CalcuMancia</h1>', unsafe_allow_html=True)
    
    # Set page size
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            width: {page_width}px;
            height: {page_height}px;
            padding: 0rem;
            margin: 0 auto;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
