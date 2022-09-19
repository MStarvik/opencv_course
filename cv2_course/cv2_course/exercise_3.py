#!/usr/bin/env python3
import cv2
from pathlib import Path

cv2_data_path = Path(cv2.__file__).parent / "data"
if not cv2_data_path.exists():
    cv2_data_path = Path("/usr/local/share/opencv4/haarcascades")

face_cascade_path = str(cv2_data_path / "haarcascade_frontalface_alt2.xml")
