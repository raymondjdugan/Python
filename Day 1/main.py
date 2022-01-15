# print("Hello World")
# print("Day 1 - Python Print Function")
# print("The function is declared like this:")
# print("print('what to print')")
# print("Day 1 - String Manipulation")
# print('String Concatenation is done with the "+" sign')
# print('e.g. print("Hello " + "world")')
# print("New lines can be created with a backslash and n.\n")
# input() will get the input in the compiler
# print() will print the number of letters in the name entered
print(len(input("What is your name?\n")))
name = input("What is your name?")
print(name)
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
