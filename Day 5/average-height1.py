
# this solution using the sum and len functions

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

average = sum(student_heights) / len(student_heights) # add and divide the list

print("The average height is ", round(average)) # print out the rounded result
