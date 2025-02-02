#! python 3

#resizeAndAddLogo.py - resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok = True)
#TODO: Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
       or filename == LOGO_FILENAME:
        continue #skip non-image files and the logo file itself.

    im = Image.open(filename)
    width, height = im.size

    
#TODO: Check if image nees to be resized.
if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
    #Calculate the new width and height to resize to.
    if width > height:
        height = int((SQUARE_FIT_SIZE / width) * height)
        width = SQUARE_FIT_SIZE
    else:
        width = int((SQUARE_FIT_SIZE / height) * width)
        height = SQUARE_FIT_SIZE

    #resize the image.
    print('Resizing %s...' %(filename))
    im = im.resize((width, height))


    #Add the logo
    print('Adding logo to %s...') % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    #save changes.
    im.save(os.path.join('withLogo', filename))

    #add the logo
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - lgoWidth, height - logoHeight), logoIm)

    #Save Changes
    im.save(os.path.join('withLogo', filename))

