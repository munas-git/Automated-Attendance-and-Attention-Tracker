# Importing Important Libraies
import os
import cv2
import numpy as np
import face_recognition
from datetime import datetime


# Capturing video
live_capture = cv2.VideoCapture(0)

# Face encoding
img = cv2.imread("test-images/Einstein.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
einstein_encoding = face_recognition.face_encodings(rgb_img)[0]
known_names = ['Einstein']


# Looping through frames and performing verification
while True:
    _, frame = live_capture.read()

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Looping through all identified faces.
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        
        # Check for matching known faces?
        matches = face_recognition.compare_faces([einstein_encoding], face_encoding)

        name = "Unregistered Student"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

        # Drawing bounding box
        cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    
    cv2.imshow("Attendance Logger", frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


live_capture.release()
cv2.destroyAllWindows()