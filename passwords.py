from string import ascii_letters, digits
import random


letters = list(ascii_letters)
numbers = list(digits)
special = list("!?/&$-_")

password = list()

for i in range(8):

    if i == 0 or type == 1:
        pos = random.randint(0, len(letters)-1)
        password.append(letters[pos])
    elif i == 1 or type == 2:
        pos = random.randint(0, len(numbers)-1)
        password.append(numbers[pos])
    elif i == 2 or type == 3:
        pos = random.randint(0, len(special)-1)
        password.append(special[pos])
    else:
        type = random.randint(1, 3)

random.shuffle(password)

string = ""

for letter in password:
    string += letter

print(string)

