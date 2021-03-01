# adding the even numbers between 1 and 100 together

even_num = 0
for number in range(1,101):
  if number % 2 == 0:
    even_num += number
print(even_num)


# second method

even_num = 0
for number in range(1,101,2):
    even_num += number
print(even_num)
