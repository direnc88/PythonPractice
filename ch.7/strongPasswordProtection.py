#strongPasswordProtection.py

import re

def detectPassword(text):
    #should make sure pw is 8 chars
    #eightCharsRegex = re.compile(r'''([a-ZA-Z0-9._%+-]{8,})''')
    #if not(eightCharsRegex.search(text)):
        #print("Please make sure your password is at least 8 characters long.")
        #return False

    if len(text) < 8:
        print("Please make sure your password is at least 8 characters long.")
        return False

    #checks for lower case letters
    lowerReg = re.compile(r'''[a-z]''')
    if not(lowerReg.search(text)):
        print("Please make sure your password has at least one lower case letter.")
        return False
    
    #checks for upper case letters. 
    upperReg = re.compile(r'''[A-Z]''')
    if not(upperReg.search(text)):
        print("Please make sure your password has at least one upper case letter.")
        return False
    
    #should make sure the pw has one number. 
    numberRegex = re.compile(r'\d+')
    if not(numberRegex.findall(text)):
        print("Please make sure your password has at least one number.")
        return False

print("Please enter a password that is 8 characters, has one uppercase letter, one lowercase letter and a number: ")  
text = input()
#if detectPassword(text):
  #  print("Your Password is strong!")

  # should probably figure out a way to tell the user that their password is strong. 
