#Coding the second part of the hangman game

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.\n')


display = list() #create an empty list

for letter in (chosen_word): #create hangman grid to show the use how many words need to be guessed
  display += ("_")
print(display)


guess = input("Guess a letter: ").lower() #user guesses a letter

for position in range(len(chosen_word)): #if the letter is in the word, put the letters into the grid
    if chosen_word[position] == guess:
        display[position] = guess

print(display)





