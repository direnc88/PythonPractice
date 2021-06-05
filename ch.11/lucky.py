#! python 3

#lucky.py - opens several google search results

#gets search keywarods from the command line arguments
#retrieves the search results page.
#opens a browser tab for each result.

import requests, sys, webbrowser, bs4

print('Googling...') #display text while downloading the Google Page. 
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#TODO: Retrieve top search result links.

#TODO: Open a broswer tab for each result.

