# Data Types
# String, Integer, Float and Boolean

# #String
# print("Hello"[4])

# #interger
# print(123 + 345)
# 123_456_789

# #Float
# 3.14159

# #Bolean
# True
# False


# Type conversion

# num_char = len(input("What is your name"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters")

# a = float(123)
# print(type(a))

# print(70 + float("100.5"))
# print(str(70) + str(100))

# Mathematical Operation
# Addition 3 + 5
# Subtraction 3 - 5
# Multiplication 3 * 2
# Division 6 / 3
# Exponents 2 ** 3

# Number Manipulation and F Strings in Python

# print(round(2.6666666, 2))
# print(4 / 2)

# result = 4 / 2
# result /= 2
# print(result)

# f-string
score = 0
height = 1.8
isWinning = True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# Exercise 1:
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

num_one = int(two_digit_number[0])
num_two = int(two_digit_number[1])
num_equal = num_one + num_two

print(str(num_one) + " + " + str(num_two) + " = " + str(num_equal))

# Exercise 2:
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)

print(bmi)

# Exercise 3:
# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

age_as_int = int(age)
years = 90 - age_as_int
months = years * 12
weeks = years * 52
days = years * 365

message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)
