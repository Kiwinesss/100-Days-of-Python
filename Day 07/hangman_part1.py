#Coding the first part of the hangman game


import random

word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
for word in word_list:
  chosen_word = random.choice(word_list)

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Choose a letter: ").lower()

#Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
  if guess == letter:
    print("yes")
  else:
    print("no")
    
    
    
    
