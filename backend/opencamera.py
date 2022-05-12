import cv2
from funciones import find_des, find_id
from featuresimg import images, class_names

deslist = find_des(images) 

cap = cv2.VideoCapture(0)

while True:

    success, img2 = cap.read()
    img_original = img2.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    id = find_id(img2, deslist)
    if id != -1:
        cv2.putText(img_original, class_names[id], (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)

    cv2.imshow("img2", img_original)
    cv2.waitKey(1)