# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
row = int(position[0])
col = int(position[1])
row_adjusted = (row -1)
col_adjusted = (col -1)
map[row_adjusted][col_adjusted] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


##########################################

#This below was my first attemp, many lines of ugliness

##########################################

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

coll = int(position[0])
row = int(position[1])

if row == 0 and coll == 0:
    row1[coll] = "X"
elif row == 0 and coll == 1:
    row1[coll] = "X"
elif row == 0 and coll == 2:
    row1[coll] = "X"

if row == 1 and coll == 0:
    row2[coll] = "X"
elif row == 1 and coll == 1:
    row2[coll] = "X"
elif row == 1 and coll == 2:
    row2[coll] = "X"

if row == 2 and coll == 0:
    row3[coll] = "X"
elif row == 2 and coll == 1:
    row3[coll] = "X"
elif row == 2 and coll == 2:
    row3[coll] = "X"

print(f"{row1}\n{row2}\n{row3}")




