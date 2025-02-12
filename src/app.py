import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pickle
import streamlit as st
import numpy as np

st.markdown(
    """
    <style>
    .stApp {
        background: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZ7FimwPty6Ci2Lq_YzVCZ08TQbIn4_bHejQ&s') repeat center center fixed;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)



def main():
    st.title('Bienvenido al portal "Ponte guap@"')
    st.write('**Por favor selecciona uno de nuestros servicios**')
    
    opcion = st.radio('Seleccione el servicio:', 
                      ('Sube una foto para ver si vas combinad@', 'Dime que colores llevas', 'Dame un consejo para estar más Guap@'), 
                      index=0, 
                      key='option')
    
    if st.button('Empezar!'):
        route_prediction(opcion)


def route_prediction(opcion):
    if opcion == 'Sube una foto para ver si vas combinad@':
        switch_page("pred_imagen")
    elif opcion == 'Dime que colores llevas':
        switch_page("pred_colores")
    elif opcion == 'Dame un consejo para estar más Guap@':
        switch_page("pred_consejo")
 
if __name__ == "__main__":
    main()

