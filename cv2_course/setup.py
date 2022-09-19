#!/usr/bin/env python3
import setuptools

setuptools.setup(
    name='cv2_course',
    version='0.1',
    description='Utilities for OpenCV course',
    author='Mikkel Stårvik',
    author_email='mikkel.starvik@gmail.com',
    packages=['cv2_course'],
    package_data={"cv2_course": ["*.npy"]}
)