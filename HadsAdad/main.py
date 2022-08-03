import math
from random import random

randomNum = max(0, min(int(random()), 100))


def checkNumber(num):
    if num == randomNum:
        return 1
    elif num < randomNum:
        return 0
    else:
        return -1


while True:
    guess = int(input("Enter ur guess in [0,100]: "))
    if checkNumber(guess) == 1:
        print("that's right")
        break
    elif checkNumber(guess) == 0:
        print("say bigger")
    else:
        print("say smaller")


