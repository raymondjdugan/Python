# If/Else Statements
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Nested If/Else statement and elif
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Multiple if statements
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += + 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

# Logical Operators
# and
# or
# not

# Exercise 1:
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Exercise 2:
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <22:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <28:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 33:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# Exercise 3:
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

a = year % 4
b = year % 100
c = year % 400

if a == 0:
    if b == 0:
        if c == 0:
            print("Leap Year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# Exercise 4:
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}.")

# Exercise 5:
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

name_low = name1 + name2
name_lower = name_low.lower()

t = name_lower.count("t")
r = name_lower.count("r")
u = name_lower.count("u")
e = name_lower.count("e")

true = t + r + u + e

l = name_lower.count("l")
o = name_lower.count("o")
v = name_lower.count("v")
e = name_lower.count("e")

love = l + o + v + e

love_total = int(str(true) + str(love))


if(love_total < 10) or (love_total >= 90):
    print(f"Your score is {love_total}, you go together like coke and mentos.")
elif love_total >=40 and love_total <=50:
    print(f"Your score is {love_total}, you are alright together.")
else:
    print(f"Your score is {love_total}.")
