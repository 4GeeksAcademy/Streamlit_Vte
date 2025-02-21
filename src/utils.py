import pickle
import streamlit as st
import numpy as np
import random

def predict_consejo():
    # Coge una frase del string aleatoria
    consejos = ['Vístete según tu talla, no la que deseas tener.',
                 'El negro adelgaza, pero no hace milagros.', 
                 'Si dudas, ponte jeans; nunca fallan.',  
                 "Las chanclas son para la playa, no para la ciudad.",
                 "Las marcas no hacen estilo, tu actitud sí.",
                 "Combinar estampados es arte, o un desastre.",
                 "Zapatos limpios, porque todos los miran sin que lo notes.",
                 "La moda pasa, las fotos quedan. Piénsalo."]

    return random.choice(consejos)

def predict_imagen(imagen):
       
    # Obtener el nombre de la clase predicha
    class_names = ['Vas super guap@', 'Pichi pichá', 'Fatal de la muerte', 'No te atrevas a salir de casa']
    return random.choice(class_names)

def check_colores(color1,color2):
    
    combinan = [("Rojo", "Negro"), ("Azul", "Blanco"), ("Verde", "Amarillo"), ("Negro", "Blanco")]
    
    if color1 and color2:
        if (color1, color2) in combinan or (color2, color1) in combinan:
            st.success(f"¡Buena elección! {color1} y {color2} combinan bien.")
        elif color1==color2:
            st.warning("Sé un poquitín mas original")
        else:
            st.warning(f"{color1} y {color2} no combinan muy bien.")

#def check_client_id(client_id):
    # Simulación
    # Cargar credenciales para la BBDD de la empresa y consultar si el identificador del cliente está activo 
    #api_key = st.secrets["DB_USERNAME"]
    #ls_ids = [123,12345,12345678]
    #return True if client_id in ls_ids else False
    
#print(f"TensorFlow version: {tf.__version__}")
