<div align="center">

# Image-duplicate-remover

</div>
<p align="center">
  <img src="https://raw.githubusercontent.com/AydenBravender/Image-duplicate-remover/main/Screenshot%202023-09-28%20171000.jpg" alt="Example Tkinter window" width="50%" height="50%">>
</p>

## Overview

This program removes duplicates of images within a folder. It ultilizes Tkinter, os, and OpenCV. It will skip over folders, .txt files and any other files that are not '.jpg', '.jpeg' and '.png'. To this end the program resizes each image to a 1 x 1 pixel, and compares RGB values in order to determine if something is a match. There are over 16 000 000 possible values for the RGB values, However if you would rather you could edit the code to resize the image to a 2 x 2.

## What It Removes:
What it will remove:
- Rotated Images that are duplicates of images.
- Different image types (.jpg, .png, .jpeg)
- Resized Images (only if they are resized using cv2 function, using Pillow doesn't work)
- And the same image

## Dependencies:
install ```os```, ```Tkinter``` and```OpenCV```
  

## Terms and Conditions:
This code could potentially delete useful files, images or other information. I am not at fault for you using this code.




