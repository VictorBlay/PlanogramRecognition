from json import detect_encoding
from typing import final
from matplotlib.pyplot import cla
import numpy as np
import cv2
import os


path = "queryimage"
imagenes = [imagenes for directorio, subdirectorio, imagenes in os.walk(path)]
direct = [subdirectorio for directorio, subdirectorio, imagenes in os.walk(path)]


aplanar_lista = lambda lista: [elemento for sublista in lista for elemento in sublista]


images = []
class_names = []
list_img = aplanar_lista(imagenes)
list_dir = aplanar_lista(direct)
for dir in list_dir:
    for cl in list_img:
        img_cur = cv2.imread(f"{path}/{dir}/{cl}", 0)
        images.append(img_cur)
    class_names.append(os.path.splitext(dir)[0])