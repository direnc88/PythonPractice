#phoneAndEmail.py - Find phone numbers and email adress on the clip board.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(|d{3}\))           #area code
    (\s|-|\.)?                  #separator
    (\d{3})                     #first 3 digits
    (\s|-|\.)                   #separator
    (\d{4})                     #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    #extension
    )''', re.VERBOSE)

# TODO: Create email regex
#create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+     #username
    @                     #the @ symbol
    [a-zA-Z0-9.-]+        #domain name
    (\.[a-zA-Z]{2,4})     #dot-something
    )''', re.VERBOSE) 


# TODO: Find matches in clipboard text

##The phone number string is built of groups 1, 3, 5, and 8. It is the
##area code, first three digits, last four digits, and the extensoin. The first group,
##group[0] is the entire string.  

text = str(pyperclip.paste())
    matches = []
    for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


# TODO: Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('no phone numbers or email addresses found.')
