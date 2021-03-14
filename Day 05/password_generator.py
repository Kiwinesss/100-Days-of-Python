#Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# create the password using a user-stipulated combination of random characters from the lists of letters, numbers and symbols

characters = ""
for letter in range(0,nr_letters):
    characters += random.choice(letters)

for number in range(0,nr_numbers):
    characters += random.choice(numbers)

for symbol in range(0,nr_symbols):
    characters += random.choice(symbols)

#randomise the order of the created password.

char_list = list(characters) # convert string into list

random.shuffle(char_list)

final_str = ''.join(char_list) # convert list to string

print(final_str)












