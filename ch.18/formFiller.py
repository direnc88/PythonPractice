#! python 3

#formFiller.py - Automatically fills in the form.

#Raise the cursor to the upper left hand side of the screen to activate failsafe. 

import pyautogui, time

#Set these to the correct coordinates for your computer.
nameField = (648, 319)
submitButton = (651, 817)
submitButtonColor = (75, 141, 249)
submitAnotherLink = (760, 224)

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'}
            ]


pyautogui.PAUSE = 0.5


for person in formData:
    #Give the user a chance to kill the script.
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)

    #wait until the page has loaded
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        time.sleep(5)


    print('Entering %s info...' % (person['name']))
    pyautogui.click(nameField[0], nameField[1])

    #fill out the Name Field.
    pyautogui.typewrite(person['name'] + '\t')

    #fill out the Greatest Fear Field.
    pyautogui.typewrite(person['fear'] + '\t')

    #fill out the Source of Wizard Powers field.
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', '\t'])

    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', '\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])

    #fill out the Robocop field.
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

    #fill out the additional comments field.
    pyautogui.typewrite(person['comments'] + '\t')

    #click submit.
    pyautogui.press('enter')

    #wait until form page has loaded.
    print('Clicked Submit.')
    time.sleep(5)

    #click the submit another response link
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])

