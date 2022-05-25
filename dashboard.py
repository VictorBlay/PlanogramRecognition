import py_compile
from cv2 import find4QuadCornerSubpix
import streamlit as st
from PIL import Image
import cv2
from backend import funciones, description


path = "./backend/queryimage"

page = st.sidebar.selectbox('Categoria gestionada ', 
            ['Salud Ocular',
            'Dolor',
            'Higiene Bucodental',
            'Insomnio',
            'Invierno',
            'Mosquitos',
            'Piojos',
            'Probioticos',
            'Solares'])

if page == 'Salud Ocular':
    def main_loop():
        st.title("OpenCV Demo App")
        st.subheader("Esta app te permite saber el uso de los productos de parafarmacia que podras encontrar en nuestras oficinas de farmacia!")
        st.text("Usamos OpenCV y Streamlit para esta demo")

        st.title("Escanear Producto")
        run = st.checkbox('Encender camera')
        FRAME_WINDOW = st.image([])
        camera = cv2.VideoCapture(0)
        deslist = funciones.find_des(funciones.imagenes(path))
        desc = st.empty()

        while run:
            _, frame = camera.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            id = funciones.find_id(frame, deslist)
            

            if id != -1:
                cv2.putText(frame, funciones.car_prod(path)[id], (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,178,169), 1)
                desc.text(description.description_product(funciones.car_prod(path)[id]))
            FRAME_WINDOW.image(frame)
            
        else:
            st.write('Apagada')

    if __name__ == '__main__':
        main_loop()