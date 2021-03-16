from game_data import data
from art import logo, vs
import random
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

score = 0
def random_name():
  return random.randint(0,(len(data)-1)) 
  
def user_information():
  x = random_name()
  username = data[x]["name"]
  user_description = data[x]["description"]
  user_country = data[x]["country"]
  user_follower_count = data[x]["follower_count"]
  return username, user_description, user_country, user_follower_count      
 
current_answer = False                                                                   
 
def calculation(score,name1,description1,country1, follower_count1,name2,description2,country2,follower_count2):
      cls()
      print(logo)
      if current_answer == True:
        score += 1
        print(f"You're right! Current score: {score}")
        name1 = name2 
        description1 = description2
        country1 = country2
        follower_count1 = follower_count2
      print(f"Compare A: {name1}, a {description1}, from {country1} ")
      user_information()
      name2, description2, country2, follower_count2 = user_information()
      print(vs)
      print(f"Against B: {name2}, a {description2}, from {country2}  ")
      return score, follower_count1, name2, description2, country2, follower_count2  
 
name1, description1, country1, follower_count1 = user_information()
name2, description2, country2, follower_count2 = user_information()
 
calculation(score,name1,description1,country1, follower_count1,name2,description2,country2,follower_count2)
 
current_answer = True
 
while current_answer == True:
  user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
  if follower_count1 > follower_count2:
      if user_input == "a":
        calculation(score,name1,description1,country1, follower_count1,name2,description2,country2,follower_count2)
        score,follower_count1, name2, description2, country2, follower_count2  = calculation(score,name1,description1,country1, follower_count1,name2,description2,country2,follower_count2)
      else:
        current_answer = False
  
  elif follower_count1 < follower_count2:
    if user_input == "b":
        calculation(score,name1,description1,country1, follower_count1,name2,description2,country2,follower_count2)
        score, follower_count1, name2, description2, country2, follower_count2 = calculation(score,name1,description1,country1, follower_count1,name2,description2,country2,follower_count2)
    else: 
      current_answer = False
  else:
    current_answer = False
 
if current_answer == False:
  cls()
  print(logo)
  print(f"Sorry, that's wrong. Final score: {score}")
  
  
  
  
