from json import detect_encoding
from typing import final
from matplotlib.pyplot import cla
import numpy as np
import cv2 as cv
import os

path = "queryimage"
orb = cv.ORB_create()

images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    imgCur = cv.imread(f"{path}/{cl}", 0)
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])

#separar funciones y mayusculas
#unit
def findDes(images):
    desList = []
    for img in images:
        kp, des = orb.detectAndCompute(img, None)
        desList.append(des)
    return desList

def findID(img, desList, thres = 15):
    kp2, des2 = orb.detectAndCompute(img, None)
    bf = cv.BFMatcher()
    matchList = []
    finalVal = -1
    try:
        for des in desList:
            matches = bf.knnMatch(des, des2, k=2)
            good = []
            for m,n in matches:
                if m.distance < 0.75*n.distance:
                    good.append([m])
            matchList.append(len(good))
    except:
        pass
    if len(matchList) != 0:
        if max(matchList) > thres:
            finalVal = matchList.index(max(matchList))
    return finalVal

desList = findDes(images) 

cap = cv.VideoCapture(0)

while True:

    success, img2 = cap.read()
    imgOriginal = img2.copy()
    img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

    id = findID(img2, desList)
    if id != -1:
        cv.putText(imgOriginal, classNames[id], (50,50), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)

    cv.imshow("img2", imgOriginal)
    cv.waitKey(1)