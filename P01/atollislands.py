

import random

def generate_iban_numb(iterations):
    numbs = ""
    for i in range(iterations):
        numbs += str(random.randint(0,9))

    return numbs

print(generate_iban_numb(3))