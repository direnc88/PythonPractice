#coinTossDebug.py

#this is a practice program to debug.

#This is a coin toss debugging game. The player gets two guesses, but I am to find all the errors in the program that keep it
#from running.

import random, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - ' '%(levelname)s - %(message)s') 

logging.debug('Start of program')

guess = ''
while guess not in ('heads', 'tails'):
    logging.debug('Start of guess')
    print('Guess the coin toss! enter heads or tails: ')
    guess = input()

logging.debug('Start of coin toss')
toss = random.randint(0, 1) # 0 is tails, 1 is heads

#this was added. Needed to turn the 0 and the 1 to heads and tails. 
if toss == 0:
    toss = 'tails'
if toss == 1:
    toss = 'heads'
    
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()   #there are 3 s' instead of two.
    if toss == guess:  #there was one equals symbol here instead of two. 
        print('You got it!')
    else:
        print('Nope. you are really bad at this game.')
