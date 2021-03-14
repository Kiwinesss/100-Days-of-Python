# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? s, m, or l ")
add_pepperoni = input("Do you want pepperoni? y or n ")
extra_cheese = input("Do you want extra cheese? y or n ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "s":
  bill += 15
  if add_pepperoni == "y":
    bill += 2
  if extra_cheese =="y":
    bill += 1
    print(f"Your bill comes to ${bill}")
else:
  bill = 0



if size == "m":
  bill += 20
  if add_pepperoni == "y":
    bill += 3
  if extra_cheese =="y":
    bill += 1
    print(f"Your bill comes to ${bill}")
else:
  bill = 0



if size == "l":
  bill += 25
  if add_pepperoni == "y":
    bill += 3
  if extra_cheese =="y":
    bill += 1
    print(f"Your bill comes to ${bill}")
else:
  bill = 0






