#key:value

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}
print(programming_dictionary["Bug"]) #retrieve an entry from the dictionary using the key
print(programming_dictionary["Function"])

#adding items to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#create an empty dictionary
empty_dictionary = {}
print(empty_dictionary)

#wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#edit an item in a dictionary
programming_dictionary["Bug"] = "a different value"
print(programming_dictionary)

#loop through a empty_dictionary - only the key is printed
for key in programming_dictionary:
  print(key)

  print(programming_dictionary[key]) #this will print the value as well
