import streamlit as st
from PIL import Image
import numpy as np
from utils import predict_imagen
st.markdown(
    """
    <style>
    .stApp {
        background: url('https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLX0tM0c0ugduxnWVRTi01jT1DqVBKi26HBIg0m-QqA5rp5BpM7KFIFM8AmgsN_q2asnRBzi3ZuwLcNWEm2HjchuJSKNyr_mcUh7gzaxy4uMUmL3ncRmWZjL_IWtbT9S4bJILY90KEuWE/s1600/el-estilo-de-rafa-mora-9_1_.jpg') no-repeat center center fixed;
        background-size: contain;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Título de la aplicación
st.title('¿Vas combinad@?')

# Cargar la imagen
uploaded_file = st.file_uploader("Cargar imagen", type=["jpg", "jpeg", "png"])

# Si se carga una imagen
if uploaded_file is not None:
    # Mostrar la imagen
    st.write('**Vista Previa de la imagen cargada:**')
    image = Image.open(uploaded_file).resize((32, 32))
    st.image(image, caption='Imagen cargada', use_column_width=True)

    # Convertir la imagen a una matriz de valores de píxeles
    image = np.array(image) / 255.0  # Normalizar los valores de píxeles
    
    # Botón para realizar la predicción con las columnas seleccionadas
    if st.button('Realizar Predicción de la categoría de la imagen'):
        # Predecirla
        pred = predict_imagen(image)

        # Mostrar los resultados de la predicción
        st.success('Éxito al realizar la predicción!')
        st.write('La categoría predicha para la imagen:')
        st.write(pred)