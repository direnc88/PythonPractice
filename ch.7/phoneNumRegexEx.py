import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#or I could use r'\d{3}-\d{3}-\d{4}'
mo = phoneNumregex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
#dont forget to try regexpal.com
