import cv2
 
capture = cv2.VideoCapture(0)

while (True):
    ret, frame = capture.read()
 
    cv2.imshow('Test hand', frame)
 
    if cv2.waitKey(1) == 27:
        break
 
cv2.destroyAllWindows()
capture.release()