print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride on the rollercoaster")
    age = int(input("How old are you?: "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        print("Midlife crisis victims can enter for free") 
    else:
        bill = 12
        print("Adult tickets are $12")
    photo = input("Would you like  a photo? (y/n): ")
    if photo == "y":
        bill += 3
        print(f"Please pay ${bill}")
    else:
        print(f"Please pay ${bill}")

else:
    print("Come back when you have grown taller laddie")

    
    
    
    
    
