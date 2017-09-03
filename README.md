# SetGame
A Python program to find sets in the card game "Set" based off an image

The result of src2.py when used with gameimg8.jpeg is shown in the image below. This program is used when the cards are spaced out. 

![set_game_results](https://user-images.githubusercontent.com/12382926/30002606-180c4afe-9073-11e7-9dda-0b60acbc6c08.jpg)

The result of src.py when used with gameimg1.jpg is shown below. This is used when the cards are all next to each other in a 4x3 array. 

![set_game_results](https://user-images.githubusercontent.com/12382926/30002644-1a454e5a-9074-11e7-802c-efe6fd99c42e.jpg)

This program relies on image processing techniques such as contour detection, canny edge detection, color masking, and OpenCV's built in matchTemplate function. As a result, performance may degrade in varying lighting conditions. A machine learning solution using Haar Cascades is currently being built. 
