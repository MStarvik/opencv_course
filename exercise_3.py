#!/bin/env python3
import cv2

from pathlib import Path

cv2_data_path = Path(cv2.__file__).parent / "data"
if not cv2_data_path.exists():
    cv2_data_path = Path("/usr/local/share/opencv4/haarcascades")

face_cascade_path = cv2_data_path / "haarcascade_frontalface_alt2.xml"
# face_cascade_path = cv2_data_path / "haarcascade_smile.xml"
# eye_cascade_path = cv2_data_path / "haarcascade_smile.xml"
# eye_cascade_path = cv2_data_path / "haarcascade_eye.xml"
# eye_cascade_path = cv2_data_path / "haarcascade_smile.xml"

face_cascade = cv2.CascadeClassifier(str(face_cascade_path))
# eye_cascade = cv2.CascadeClassifier(str(eye_cascade_path))

img = cv2.imread("images/concept_review.jpg", cv2.IMREAD_COLOR)
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

cv2.imshow("image", img)
cv2.waitKey()