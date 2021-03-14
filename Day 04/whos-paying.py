# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
name = random.randint(0,len(names))
payer = names[name]
print(f"{payer} will be paying for your meal today!")




