import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
from art import logo
import random

print(logo)

print("What is my number?  It is somewhere between 1 and 100.")
user_choice = input("Are you a man or a mouse? Type 'mouse' or 'man': ").lower()
if user_choice == 'mouse':
  guesses = 10
  print("You have 10 shots at guessing my number.")
if user_choice == 'man':
  guesses = 5
  print("You have 5 shots at guessing my number.")
number = random.randint(1, 100)

guess = int(input("Have a guess: "))
while guesses >= 1:
  if guess == number:
    print("Bingo! The answer was", number)
    guesses = 0
  elif guess < number:
    guesses -= 1
    print("Too low!")
    print(f"You have {guesses} attempts left")
    if guesses >= 1:
      guess = int(input("Guess again:"))
    else:
      print("You have no more guesses. You lose!")
  elif guess > number:
    guesses -= 1
    print("Too high!")
    print(f"You have {guesses} attempts left")
    if guesses >= 1:
      guess = int(input("Guess again:"))
    else:
      print("You ran out of guesses. You lose!")
      
      
      
