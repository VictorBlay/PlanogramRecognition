import os
import cv2
import glob
import numpy as np
import re

def prepare_data(images_path):
    m = f"{images_path}/**/*.jpg"
    x = [os.path.normpath(i) for i in glob.glob(m, recursive=True)]
    carpetas = []
    for i in x:
        medicamento = i.split("\\")[2]
        carpetas.append(medicamento)
    
    result = list(zip(x, carpetas))
    return result