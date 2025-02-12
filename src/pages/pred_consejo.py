import streamlit as st
import numpy as np
from utils import predict_consejo
st.markdown(
    """
    <style>
    .stApp {
        background: url('https://blog.sight-management.com/wp-content/uploads/2014/05/adrien_brody_big_black_book_photos_002-600x721.jpg') no-repeat center center fixed;
        background-size: contain;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.title('¿Quieres un consejo?')

if st.button('Dame un consejo sobre moda'):
    consejo = predict_consejo()
    st.write(consejo)
