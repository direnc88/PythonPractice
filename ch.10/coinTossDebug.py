#coinTossDebug.py

#this is a practice program to debug.

#This is a coin toss debugging game. The player gets two guesses, but I am to find all the errors in the program that keep it
#from running.

import random, logging

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()   #there are 3 s' instead of two.
    if toss = guess:
        print('You got it!')
    else:
        print('Nope. you are really bad at this game.')
