# RANDOM
import random

random_integer = random.randint(1, 100)
print(random_integer)

random_float = random.random() * 5
print(random_float)

# LIST
fruits = ["Cherry", "Apple", "Banana"]
states_of_america = ["Delaware", "Pennsylvania"]

states_of_america[0]  # Positive number will pull from the beginning of the LIST
states_of_america[-1]  # Negative number will pull from the end of the list

# Adding to a List

states_of_america.append("NewState")  # Append will add to the end of the list
states_of_america.extend("NewState1", "NewState2")  # Will extend the list

# Nested List
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]

# Exercise 1:
# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

rand_side = random.randint(0, 1)

if rand_side == 0:
    print("Heads")
else:
    print("Tails")

# Exercise 2:
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
length_of_list = len(names)
random_int = random.randint(0, length_of_list - 1)
who_is_paying = names[random_int]
message = f"{who_is_paying} is going to buy the meal today!"

print(message)

# Exercise 3:
# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
column_int = int(position[0])
row_int = int(position[1])

map[row_int - 1][column_int - 1] = "X"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
