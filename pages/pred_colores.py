import streamlit as st

# Título de la aplicación
st.title('¿Vas combinado?')

# Lista de colores disponibles
colores = ["Rojo", "Azul", "Verde", "Amarillo", "Negro", "Blanco"]

# Botones para elegir colores
color1 = st.radio("Selecciona el primer color:", colores)
color2 = st.radio("Selecciona el segundo color:", colores)

# Botón para validar la entrada
if st.button("Verificar colores"):
    if color1 and color2:
        st.success(f"Has elegido los colores: {color1} y {color2}")
    else:
        st.error("Debes seleccionar dos colores.")

