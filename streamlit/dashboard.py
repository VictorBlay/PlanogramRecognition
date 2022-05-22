import py_compile
from cv2 import find4QuadCornerSubpix
import streamlit as st
from PIL import Image
import cv2

page = st.sidebar.selectbox('Categoria gestionada ', 
            ['Dolor',
            'Higiene Bucodental'
            'Insomnio',
            'Invierno',
            'Mosquitos',
            'Piojos',
            'Probioticos',
            'Salud Ocular',
            'Solares'])

if page == 'Salud Ocular':
    def main_loop():
        st.title("OpenCV Demo App")
        st.subheader("Esta app te permite saber el uso de los productos de parafarmacia que podras encontrar en nuestras oficinas de farmacia!")
        st.text("We use OpenCV and Streamlit for this demo")

        st.title("Webcam Live Feed")
        run = st.checkbox('Run')
        FRAME_WINDOW = st.image([])
        camera = cv2.VideoCapture(0)

        while run:
            _, frame = camera.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(frame)
        else:
            st.write('Stopped')
        

        original_image = Image.open(image_file)
        original_image = np.array(original_image)

        processed_image = blur_image(original_image, blur_rate)
        processed_image = brighten_image(processed_image, brightness_amount)

        if apply_enhancement_filter:
            processed_image = enhance_details(processed_image)

        st.text("Original Image vs Processed Image")
        st.image([original_image, processed_image])


    if __name__ == '__main__':
        main_loop()