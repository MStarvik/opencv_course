#!/usr/bin/env python3
import cv2
from pathlib import Path

data_path = Path(cv2.__file__).parent / "data"
if not data_path.exists():
    data_path = Path("/usr/local/share/opencv4/haarcascades")

cascade_paths = {}
for cascade_path in data_path.glob("*.xml"):
    cascade_name = "_".join(cascade_path.stem.split("_")[1:])
    cascade_paths[cascade_name] = cascade_path
