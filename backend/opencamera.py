from multiprocessing.spawn import prepare
import cv2
from funciones import find_des, find_id
from prepare_data import prepare_data

path = "./queryimage"

def open_camera(path):
    ruta_img = [i[0] for i in prepare_data(path)]
    carpetas = [i[1] for i in prepare_data(path)]

    imagenes = []
    for i in ruta_img:
        cap = cv2.imread(i)
        imagenes.append(cap)

    cap = cv2.VideoCapture(0)

    deslist = find_des(imagenes)

    while True:

        success, img2 = cap.read()
        img_original = img2.copy()
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        id = find_id(img2, deslist)
        if id != -1:
            text_product = cv2.putText(img_original, carpetas[id], (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)
            text_product

        cv2.imshow("img2", img_original)
        cv2.waitKey(1)

open_camera(path)