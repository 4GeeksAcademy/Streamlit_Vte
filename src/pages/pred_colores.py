import streamlit as st
from utils import check_colores

# Título de la aplicación
st.title('¿Vas combinado?')

# Lista de colores disponibles
colores = ["Rojo", "Azul", "Verde", "Amarillo", "Negro", "Blanco"]

# Botones para elegir colores
color1 = st.radio("Selecciona el primer color:", colores)
color2 = st.radio("Selecciona el segundo color:", colores)

# Botón para validar la entrada
if st.button("Verificar colores"):
   check_colores(color1,color2)

