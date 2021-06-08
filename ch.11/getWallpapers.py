#! python3

#getWallpapers.py - downloads wallpapers from imgur

#loads the imgur home page

#searches for 3440x1440 wallpapers

#clicks on first result

#saves the images from the page (loop this?)

import requests, os, bs4

url = 'https://imgur.com/'  #starting url
os.makedirs('NewWallpapers', exist_ok = True) #store pictures in ./NewWallpapers

def getWallpapers():
    
