
# this solution without using the sum and len functions
import statistics
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

avg = statistics.mean(student_heights)
print("The average student height is ", round(avg)) # print out the rounded result




