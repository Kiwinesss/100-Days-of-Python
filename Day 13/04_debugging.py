# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: #added "and "instead of "or"
    print("FizzBuzz")
  elif number % 3 == 0: #added "elif" instead of "if"
    print("Fizz")
  elif number % 5 == 0: #added "elif" instead of "if"
    print("Buzz")
  else:
    print([number])
    
    
    
    
    
    
    
