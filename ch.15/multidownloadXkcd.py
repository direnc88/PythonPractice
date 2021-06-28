#! python 3

#multidownloadXkcd.py - downloads all of the xkcd comics.

#loads the xkcd home page

#saves the comic image on that page.

#follows the previous comic link

#repeats until it reaches the first comic.

import requests, os, bs4

url = 'http://xkcd.com'    # starting url
os.makedirs('xkcd', exist_ok = True) #store comics in ./xkcd

def downloadXkcd(startComic, endComic):
    #while not url.endswith('#'):
    #TODO: download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)


    #TODO: Find the URL of the comic image
    comicElem = soup.select('#comic image')
    if comicElem == []
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        
        #TODO: download the image
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        
        #TODO: save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chuck in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        
    #TODO: get the prev button's url.
    #prevLink = soup.select('a[rel="prev"]')[0]
    #url = 'http://xkcd.com' + prevLink.get('href')

#print('Done.)

#TODO: Create and start the Thread Objects.
downloadThreads = []    #a list of all the Thread objects
for i in range(0, 1400, 100):    #loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()
                                      
#TODO: Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
