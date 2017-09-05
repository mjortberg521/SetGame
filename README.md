# SetGame
A Python program to find sets in the card game "Set" based off an image

The result of src2.py when used with gameimg8.jpeg is shown in the image below. This program is used when the cards are spaced out. It detects contours with areas>1000 and edges=4 to recognize cards. 

![set_game_results](https://user-images.githubusercontent.com/12382926/30041158-75ad00f0-91ad-11e7-8e24-e2c707c599a1.jpg)

The result of src.py when used with gameimg1.jpg is shown below. This is used when the cards are all next to each other in a 4x3 array. 

![set_game_results](https://user-images.githubusercontent.com/12382926/30002644-1a454e5a-9074-11e7-802c-efe6fd99c42e.jpg)

This program relies on image processing techniques such as contour detection, canny edge detection, color masking, and OpenCV's built in matchTemplate function. The OpenCV matchTemplate function does not perform well when images have sizes, orientations, and color different from the template images. As a result, performance degrades highly when images in different lighting scenarios or taken from differnt cameras are presented to the template matcher. Additionally, the variance in the number of contours on 1, 2, and 3-shaped cards was high between images. 

A machine learning solution using Haar Cascades is currently being built. This Haar Cascade program will feature a model to differentiate between cards based on the number, shade, and shape of the cards. The color attribute will be determined using the current color mask technique. A Haar Cascade solution is also anticipated to be faster than the CV matchTemplate function. 
