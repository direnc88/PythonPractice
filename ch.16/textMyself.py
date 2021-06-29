#! python 3

#textMyself.py - Defines the textmyself() function that texts a message
#passed to it as a string.

#Preset values:
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
myNumber = '+15559998888'   #this will be different.
twilionumber = '+15552225678'  #this will be different.

from twilio.rest import TwilioRestClient

def textmyself(message):
    twilioCli = twilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to = myNumber)
