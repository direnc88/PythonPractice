import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

#counts the occurances of each character in a string and puts them into a dictionary
#this is accomplished using setdefault
#pretty prints the dictionary at the end of the program. 
