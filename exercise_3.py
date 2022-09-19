#!/bin/env python3
import cv2
from cv2_course.exercise_3 import face_cascade_path

face_cascade = cv2.CascadeClassifier(face_cascade_path)
# eye_cascade = cv2.CascadeClassifier(str(eye_cascade_path))

img = cv2.imread("images/cabin_trip.jpg", cv2.IMREAD_COLOR)
img = cv2.resize(img, (720, 720))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray)

for i, (x, y, width, height) in enumerate(faces):
    center = (
        x + width // 2,
        y + height // 2
    )
    size = max(width, height)
    img = cv2.rectangle(
        img,
        (center[0] - size // 2, center[1] - size // 2),
        (center[0] + size // 2, center[1] + size // 2),
        (255, 0, 255),
        4)
    # roi = img[center[1] - size // 2:center[1] + size // 2, center[0] - size // 2:center[0] + size // 2]
    # cv2.imwrite(f"images/face_{i}.png", roi)
    # cv2.imshow("face", roi)
    # cv2.waitKey()

cv2.imwrite("images/cabin_trip_faces.jpg", img)
cv2.imshow("image", img)
cv2.waitKey()