spam = ['apples', 'bananas', 'tofu', 'cats']        
        
def addingOxford(list):
    """Take a list and put an and between the two last items and add a period"""
    length = len(list)
    count = 0
    sentence = ''
    list.insert(-1, 'and')
    for i in list:
        sentence = sentence + i + ', '
        count = count + 1
    return sentence

print(addingOxford(spam))
