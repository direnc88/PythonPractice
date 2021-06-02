#replaceStrip.py

import re

def replaceStrip(text, removeChars = ' '):
    
    strip = re.compile(r'[^'+removeChars+'].*[^'+removeChars+']')
    holder = strip.search(text)
    return holder.group()
 
    #newText = strip.search

    
