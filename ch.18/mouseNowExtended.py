#! python 3

#mouseNowExtended.py - Displays the mouse cursor's current position,
#and also gives the RGB value of the pixel under the cursor. 

import pyautogui

print('Press Ctrl-C to quit.')

#TODO: get and print the mouse coordinates.

try:
    while True:
        #TODO: Get and print the mouse coordinates
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        
except KeyboardInterrupt:
    print('\nDone.')

