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
elif (love_total >= 40) and (love_total <= 50):
    print(f"Your score is {love_total}, you are alright together.")
else:
    print(f"Your score is {love_total}.")