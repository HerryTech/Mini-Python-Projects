from random import shuffle

def getSecretNumber():
    max_number = 3
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffle(numbers)
    secret_number = ""
    for i in range(max_number):
        secret_number += str(numbers[i])
    return secret_number
        

