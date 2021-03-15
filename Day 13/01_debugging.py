############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

def my_function():
    for i in range(1,21): #the range only went up to 20, which does not include 20, so the function did not work
        if i == 20:
            print("You got it!")
my_function()


# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) #randint includes both numbers so correct would be 0-5 instead of 1-6
print(dice_imgs[dice_num])



# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

year = int(input("What's your year of birth?"))
if year >= 1980 and year <= 1994: #added two equal signs to the operators
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")
else:
    print("You are just plain old!!") #added an else statement

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

age = int(input("How old are you?")) #input should be an integer not a string
if age >= 18: # added an = sign
    print(f"You can drive at age {age}.") #put in an "f" to the f-string

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) #made = out of ==
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    new_item.append(b_list) #indented this line to keep it in the loop
  print(b_list)

mutate([1,2,3,5,8,13])




