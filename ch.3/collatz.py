#this is the collatz sequence program

def collatz(number):

    if number % 2 == 2:
        even = number // 2
        print(even)
        return even
    elif number % 2 != 0:
        odd = (3 * number + 1)
        print(odd)
        return odd
    else:
        break

userInput = int(input('Enter a number:' ))

while userInput != 1:
    collatz = collatz(userInput)
          
    
