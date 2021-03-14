import time
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# r = rock
# p = paper
# s = scissors

print("Welcome to my game of Rock, Paper, Scissors.")
time.sleep(1) # Sleep for 2 seconds
print("Let's see if you can beat me at my own game!")
time.sleep(1)
print("If you really think you are up to it, then let's do it. Try to own me!\n")
time.sleep(1) 
user_choice = input("So you start. Please choose either rock (r), paper (p) or scissors (s): ")

if user_choice != "r" and user_choice != "p" and user_choice != "s":
  print("Character not allowed! Goodbye ....")
  quit()
elif user_choice == "r":
  print(rock)
elif user_choice == "p":
  print(paper)
else:
  print(scissors)

time.sleep(1)
print("Now it's my turn, let me think ..... hmmmmmm")
time.sleep(2)
print("Remember, I did not see what you chose!")
time.sleep(1)
print("Okay, I choose .....")
time.sleep(1)


computer_choice = random.choice([rock, paper, scissors])
print(computer_choice)

if computer_choice == rock and user_choice == "p":
  print("Damn! You beat me! ")
elif computer_choice == paper and user_choice == "s":
  print("You beat me! That was just pure luck!")
elif computer_choice == scissors and user_choice == "r":
  print("Oh no you beat me! Best of three?")
elif computer_choice == rock and user_choice == "r":
    print("A draw! Come on, one more time!")
elif computer_choice == paper and user_choice == "p":
    print("Tied!")
elif computer_choice == scissors and user_choice == "s":
    print("We have the same, let's go again!")
else:
  print("Beat you sucker!!!")










