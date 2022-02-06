# Print function is print()
# Use "" or '' to enclose a string
# Use f"Some text and a {variable}" to include a variable in the output

# Example: print("Hello World")
# Exercise 1:
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# Exercise 2:
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.\n")

# Exercise 3:
# input() will get the input in the compiler
# len() will get the length of a list or string
print(len(input("What is your name?\n")))

# can save data to a variable that is declared. Example: variable_name = data
name = input("What is your name?")
print(name)

# Exercise 4:
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

temp = b
b = a
a = temp

# Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
print("Hello " + input("What is your name?"))

# input() will get user input in console
# Then print() will print the word "Hello" and the user input
print("Hello " + input("What is your name?"))
