from json import detect_encoding
from typing import final
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
from funciones import find_des, find_id
from prepare_data import prepare_data




cap = cv2.imread(prepare_data("./queryimage"))
print(cap)

deslist = find_des(cap) 

while True:

    img_original = cap.copy()
    cap = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)

    id = find_id(cap, deslist)
    if id != -1:
        cv2.putText(img_original, class_names[id], (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)

    cv2.imshow("img2", img_original)
    cv2.waitKey(0)