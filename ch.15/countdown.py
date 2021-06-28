#! python 3

#countdown.py - A simple countdown script

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1


#TODO: At the end fo the countdown, play a sound file.

