# adding the even numbers between 1 and 100 together

even_score = 0
for number in range(1,101):
  if number % 2 == 0:
    even_score += number
print(even_score)
