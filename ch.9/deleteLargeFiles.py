#deleteLargeFiles.py
#I'm not going to test this one, but this should find and then delete files with over 100MB in their file size.


import os, shutil


def deleteFiles():

    for folderName, subfolders, filenames in os.walk(os.getcwd()):
    #print('The current folder is ' + folderName)

        for file in filenames:

            if os.path.getsize(file) > 100:
                print(file + " is larger than 100MB.")

                
#TODO: I'll need to edit this. It does not print out the file names. 
