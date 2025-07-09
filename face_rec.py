import cv2
import numpy as np
from GUI import root

model = 'opencv_face_detector_uint8.pb'
model_conf = 'opencv_face_detector.pbtxt'

net = cv2.dnn.readNetFromTensorflow(model, model_conf)

CHEKED = False

cap = cv2.VideoCapture(0)

def face_detect(frame, net):
    (h,w) = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame,1.0,(300,300),[104,117,123],swapRB=False, crop=False)

    net.setInput(blob)

    detectives = net.forward()

    for i in range(0,detectives.shape[2]):
        confidence = detectives[0,0,i,2]

        if confidence > 0.6:
            return True
        
    return False

def face_check():
    global CHEKED
   

    if not cap.isOpened():
        return False
    
    ret, frame = cap.read()

    if not ret:
        return False
    
    result = face_detect(frame, net)

    if result:
        CHEKED = True
        return True
    else:
        CHEKED = False
        return False
    
# def face_check_2():
    

#     if not cap.isOpened():
#         return False
    
#     ret, frame = cap.read()

#     if not ret:
#         return False
    
#     result = face_detect(frame, net)

#     if result:
#         CHEKED = True
#     else:
#         CHEKED = False
    
#     root.after(1000, face_check_2())

def isChecked():
    global CHEKED
    return CHEKED