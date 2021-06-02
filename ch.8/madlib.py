#python3
#madlib.py - should take in .txt file and add in Nouns, adjectives, and verbs in placeholders.

file = open("madlib.txt", "r")

contents = file.read()
content_list = list(contents.split())
file.close()

print(content_list)

UserAdjective = input("Please, enter an adjective:\n")

UserNoun = input("Please, enter a noun:\n")

UserVerb = input("Please, enter a verb:\n")

UserAdverb = input("Please, enter an adverb:\n")

for word in content_list:
    if word == 'ADJECTIVE' or word == 'ADJECTIVE.':
        word = UserAdjective
    elif word == 'NOUN' or word == 'NOUN.':
        word = UserNoun
    elif word == 'VERB' or word == 'VERB.':
        word = UserVerb
    elif word == 'ADVERB' or word == 'ADVERB':
        word = UserAdverb

str1 = ' '
content_list = str1.join(content_list)

print(content_list)

f = open("madlibs.txt", "a")

f.write(content_list)

f.close()

#newContents = contents.replace("ADJECTIVE", UserAdjective)

#newContents = contents.replace("NOUN", UserNoun)

#newContents = contents.replace("VERB", UserVerb)

#newContents = contents.replace("ADVERB", UserAdverb)

#print(newContents)



