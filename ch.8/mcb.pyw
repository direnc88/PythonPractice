#python3
#multiclipboard.py - saves and loads pictures of text to the clipboard
#usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#    py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#    py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#TODO: Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
#deletes keyword if it exists in shelf. 
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcb_shelf:
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
#TODO: List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
#delete whole shelf. 
    elif sys.argv[1].lower() == 'deleteall':
        mcvShelf.clear()

mcbShelf.close()


                       

