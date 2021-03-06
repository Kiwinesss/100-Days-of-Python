
def prime_checker(number):
  if n > 1:
    for x in range(2,n):
        if (n % x) == 0:
           print(f"{n} is not a prime number")
           break
    else:
       print(f"{n} is a prime number")
  else:
    print(f"{n} is not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)



