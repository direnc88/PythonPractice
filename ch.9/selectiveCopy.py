#selectiveCopy.py
#Walks througha folder tree and searches for files with a certain file extension. Copies these files from whatever ocation that are in to a new folder. 

import os, shutil

ext = ".pdf"

newFolder = r"C:\Users\charl\OneDrive\Documents\PythonPractice\ch.9\PracticeFolder\PracticeFolder2"

for folderName, subfolders, filenames in os.walk(os.getcwd()):
    #print('The current folder is ' + folderName)

    for file in filenames:
        
        #print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

        if file.endswith(ext):

            filepath = os.path.join(os.path.abspath(folderName), file)

            shutil.copy(filepath, newFolder)
            print(f'Copied {filepath} to the new folder')



        
        #for filename in filenames:
            #print('FILE INSIDE ' + folderName + ': ' + filename)

        #if filename[-4:] == fileExt:
            #shutil.move()
    #print('') 


#works but I should double check on an error for this. It does what it needs to, but the shell throws an error after it's done.  
