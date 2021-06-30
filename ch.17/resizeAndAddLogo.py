#! python 3

#resizeAndAddLogo.py - resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

#TODO: Loop over all files in the working directory.

#TODO: Check if image nees to be resized.

#TODO: Caculate the new width and height to resize to.

#TODO: Resize the image.

#TODO: Add the logo.

#TODO: Save changes.

