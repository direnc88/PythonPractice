#! python 3

#downloadXkcd.py - downloads all of the xkcd comics.

#loads the xkcd home page

#saves the comic image on that page.

#follows the previous comic link

#repeats until it reaches the first comic.

import requests, os, bs4

url = 'http://xkcd.com'    # starting url
os.makedirs('xkcd', exist_ok = True) #store comics in ./xkcd

while not url.endswith('#'):
    #TODO: download the page

    #TODO: Find the URL of the comic image

    #TODO: download the image

    #TODO: save the image to ./xkcd.

    #TODO: get the prev button's url.

print('Done.)

