# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
combined_name = name1 + name2

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

total1 = t + r + u + e
total2 = l + o + v + e

total = int(str(total1) + str(total2))
if total < 10 or total > 90:
  print(f"Your score is {total}. You go together like coke and mentos")
elif total >= 40 and total <= 50:
  print(f"Your score is {total}. You are alright together.")
else:
  print(f"Your score is {total}.")

  
  
  
  
