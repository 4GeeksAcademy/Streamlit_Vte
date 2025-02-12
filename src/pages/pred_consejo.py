import streamlit as st
import numpy as np
from utils import predict_consejo

# Título de la aplicación
st.title('¿Quieres un consejo?')

if st.button('Dame un consejo sobre moda'):
    consejo = predict_consejo()
    st.write(consejo)
