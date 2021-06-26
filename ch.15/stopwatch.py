#! python 3

#stopwatch.py - A simple stopwatch program.

import time

#display the program's instructions
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit')

input()    #press ENTER to begin

print('Started.')
startTime = time.time() #get the first lap's start time.
lastTime = startTime
lapNum = 1

#TODO: start tracking lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end ='')
        lapNum += 1
        lastTime = time.time() #reset the last lap time.
except: KeyboardInterrupt:
    #handle the Ctrl-c exception to keep its error message from displaying.
    print('/nDone.')
        


