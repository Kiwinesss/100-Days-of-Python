#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator")

bill = float(input("How much was the bill? "))

people = int(input("How many people to pay the bill? "))

tip = int(input("How many percent tip will you pay? (10/12/15): "))

tip_factor = tip / 100 +1 
total = bill * tip_factor / people
result = format(total, '.2f')
print(f"Each person should pay ${result}")
