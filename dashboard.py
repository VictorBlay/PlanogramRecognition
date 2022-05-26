import py_compile
from cv2 import find4QuadCornerSubpix
import streamlit as st
from PIL import Image
import cv2
from backend import funciones, description


path = "./backend/queryimage"

def main_loop():
        st.title("Demo App Parapharmacy")
        st.image("./backend/data_readme/ecoceutics.jpg")
        st.subheader("Esta app te permite saber el uso de los productos de parafarmacia que podras encontrar en nuestras oficinas de farmacia!")
        st.text("Usamos OpenCV y Streamlit para esta demo!")

        st.markdown("### Escanear Producto")
        page = st.selectbox('Categoria gestionada ', 
            ['Dolor',
            'Higiene Bucodental',
            'Insomnio',
            'Invierno',
            'Mosquitos',
            'Piojos',
            'Probioticos',
            'Salud Ocular',
            'Solares'])

        if page == "Salud Ocular":
            run = st.checkbox('Encender/Apagar camera')
            FRAME_WINDOW = st.image([])
            camera = cv2.VideoCapture(0)
            deslist = funciones.find_des(funciones.imagenes(path))
            lab = st.empty()
            use = st.empty()
            desc = st.empty()


            while run:
                _, frame = camera.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                id = funciones.find_id(frame, deslist)
                

                if id != -1:
                    cv2.putText(frame, funciones.car_prod(path)[id], (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)
                    lab.text(description.laboratory(funciones.car_prod(path)[id]))
                    use.text(description.use_product(funciones.car_prod(path)[id]))
                    desc.write(description.description_product(funciones.car_prod(path)[id]))
                FRAME_WINDOW.image(frame)
                
            else:
                st.write('Apagada')

if __name__ == '__main__':
        main_loop()