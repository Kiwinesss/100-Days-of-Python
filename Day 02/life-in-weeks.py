# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

current_age = int(age)

current_age_in_months = current_age * 12

age_90_in_months = 1080


months = age_90_in_months - current_age_in_months
weeks = months * 4
days = weeks * 7

print(f"You have {months} months, or {weeks} weeks, {days} days left until you are 90 years old")




