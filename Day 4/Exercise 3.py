# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\nType in a two digit number\nFirst number is column (1-3)\nSecond number is row (1-3)\n")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
column_int = int(position[0])
row_int = int(position[1])

map[row_int - 1][column_int - 1] = "X"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
