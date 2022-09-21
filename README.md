# OpenCV Course
Before starting the course, install the *Remote - Container* extension if you have not done so already. After installing the extensions, click the icon in the lower left corner and select *Reopen in Container*.

## Exercise 1 - Reading and displaying images
In this excerice you will read images from a file and display them. This exercise is primarily meant as a test to check if your system is correctly set up to complete the course. It is also meant as an introduction to the OpenCV documentation, which you will visit frequently in your work in the perception group. Use the provided resources to complete all TODOs in exercise_1.py. When finished, run your program in any of the following ways:
- clicking the green arrow in the top-right corner.
- hitting Ctrl+F5 on your keyboard.
- running `python3 exercise_1.py` in the terminal.

When attempting to run your program for the first time you might get the warning `Authorization required, but no authorization protocol specified`, followed by the error `Can't initialize GTK backend in function 'cvInitSystem'`. This is because processes created inside the container are not authorized to communicate with your windowing system. Disable access control to your windowing system by running `xhost +` in any terminal (outside of the container). Access control can be re-enabled by at any time by running `xhost -`, .

### Resources
- [Image file reading and writing](https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html)
- [High-level GUI](https://docs.opencv.org/4.x/d7/dfc/group__highgui.html)

## Exercise 2 - Manipulating and writing images 
In this exercise you will convert color images to grayscale and write the result to a file. OpenCV does, of course, have built-in functions for color space conversions, but you will implement your own. The easiest way to convert a color image to grayscale is to compute the average of the three channels for each pixel in the image. This is the same as computing the weighted sum of the three channels, where the weights are all equal to 1/3.

Try converting an image to grayscale using the above method. You may notice that the result doesn't look quite right. This is because to our eyes, not all colours contribute equally to the perceived brightness of a scene. The color green contributes the most, followed by red, followed by blue. This phenomenon is known as perceptual luminance. To account for perceptual luminance when converting an image to grayscale, we can compute the weighted sum of the three channels using different weights for each channel. Research shows that the color red contributes about 0.2126 of the brightness, green contributes about 0.7152 and blue contributes about 0.0722.

Again, try converting an image to grayscale using the above method. Thats a lot better, but the result still doesn't look quite right. This is because images are compressed in a way that exploits the non-linear relationship between luminosity and perceived luminance. This technique is known as gamma compression. To properly account for gamma compression, we would need to compute a non-linear function the three channels for each pixel in the image. This is computationally inefficient, so instead we use a linear approximation of the non-linear function. Using this linear approximation the color red contributes about 0.299 of the brightness, green contributes about 0.587 and blue contributes about 0.114.

### Hints
- Implement a function with two arguments, a three-channel image and a tuple of three floating point numbers. The function should return a single channel image where each pixel is the weighted sum of the values of the corresponding pixel in the three-channel image. The weights should be the values in the tuple.

### Resources
- [Basic Operations on Images](https://docs.opencv.org/4.x/d3/df2/tutorial_py_basic_ops.html)

## Exercise 3 - Profile picture generator
In this exercise you will apply what you have learned about reading, manipulating and writing images to create a program for automatically creating profile pictures. To accomplish this, you will use a Haar feature-based cascade classifier. The cascade classifier is already implemented in OpenCV's object detection module, but you need to supply an XML-file with the parameters of the classifier.

When given an image, the program should detect all faces contained in it. For each face, it should crop out a square region of the image containing the face (including an appropriate margin) and write it to a file. Both the input and the outputs are color images. Use the provided resources to complete the program according to the above specification.

### Hints
- Try printing the `cascade_paths`-variable to see the list of included XML-files. Select an appropriate XML-file and tweak the arguments of the classifier until most of the faces in provided images are detected, while no false detections are returned.

- The Haar feature-based cascade classifier is a compononent in the Viola–Jones object detection framework, which is used for facial recognition in digital cameras, among other applications. For those interested in how the classifier works, the provided resource contains a short description, and includes a link to the original paper describing the classifier.

### Resources
- [Object Detection](https://docs.opencv.org/3.4/d5/d54/group__objdetect.html)