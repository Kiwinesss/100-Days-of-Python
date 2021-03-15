#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
from art import logo
import random

print(logo)

player_guess = 0
guess_num = 0
ai_num = random.randint(1,100) #1 and 100 represent the range for the random value

game_type = input("Would you like to play the easy way or the hard way? Type (easy/hard): ") #easy = 10 guesses, hard = 5 guesses

game_play = True

if game_type == "easy": # this will take the user through the easy route with 10 guesses
    for num in range(1,11):
        guess_num = int(input("What number do you guess?: "))
        if  guess_num > ai_num:
            print("Too high")
        elif guess_num < ai_num:
            print("Too low!")
        else:
            print("You guessed it!")
            break
elif game_type == "hard": # this will take the user through the hard route with only 5 guesses
    for num in range(1,6):
        guess_num = int(input("What number do you guess?: "))
        if  guess_num > ai_num:
            print("Too high")
        elif guess_num < ai_num:
            print("Too low!")
        else:
            print("You guessed it!")
            break









