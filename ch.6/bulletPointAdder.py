#! python3
#bulletPointAdder.py - Adds wikipedia bullet ponts to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# separate lines and add stars
lines = text.split('\n')
for in in range(len(lines));     #loop through all indexes in the "lines" list
    line[i] = '* ' + lines[i]    # add star to each string in "lines " list
text = '\n '.join(lines)
pyperclip.copy(text)



