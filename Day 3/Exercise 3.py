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
