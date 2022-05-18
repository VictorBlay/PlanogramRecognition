import os
import cv2
import glob
import numpy as np
import re

def convert(*args):
    """
    Returns a list of tuples generated from multiple lists and tuples
    """
    for x in args:
        if not isinstance(x, list) and not isinstance(x, tuple):
            return []

    size = float("inf")
    
    for x in args:
        size = min(size, len(x))
        
    result = []
    
    for i in range(size):
        result.append(tuple([x[i] for x in args]))
        
    return result



def prepare_data(images_path):
    m = f"{images_path}/**/*.jpg"
    x = [os.path.normpath(i) for i in glob.glob(m, recursive=True)]
    carpetas = []
    for i in x:
        y = (i[11 : ])
        z = (y[:-6])
        carpetas.append(z)
    
    result = convert(x, carpetas)
    #result = zip(a, b, c, d)
    return result


    
    #deovlver array de tuplas de dos elementos cada tupla, 1er nombre carpeta, 2n la ruta images
    
    
    """imagenes = [imagenes for directorio, subdirectorio, imagenes in x]
    direct = [subdirectorio for directorio, subdirectorio, imagenes in os.walk(path)]"""


    """aplanar_lista = lambda lista: [elemento for sublista in lista for elemento in sublista]


    images = []
    class_names = []
    list_img = aplanar_lista(imagenes)
    list_dir = aplanar_lista(direct)
    for dir in list_dir:
        for cl in list_img:
            img_cur = cv2.imread(f"{path}/{dir}/{cl}", 0)
            images.append(img_cur)
        class_names.append(os.path.splitext(dir)[0])"""