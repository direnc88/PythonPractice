#! python 3

#threadDemo.py - intended to be a demo for learning how to multithread a program. 

import threading, time

print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')
