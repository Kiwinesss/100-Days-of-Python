print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Would you like to go left or right?: \n").lower()

if direction == "left":
  decision = input("You arrive at a river. Would you like to swim or wait?:\n").lower()
  if decision == "wait":
    choice = input("A ferryman arrives to take you across the river. After walking some way on the otherside, you arrive at an old spooky castle and enter. Inside there are three doors. A yellow door, a red door and a blue door. Which door do you choose?: \n").lower()
    if choice == "red":
      print("Congratulations you have found the treasure!")
    elif choice == "yellow":
      print("You have been eaten by werewoves. Game over!")
    else:
      print("You have been burnt alive by fire breathing dragons. Game over!")
  else:
    print("You get eaten by a vampire trout fish. Game over!")
else:
  print("Whoops, you fell into a hole. Game over!")  
exit()







