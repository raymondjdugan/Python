# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

age_as_int = int(age)
years = 90 - age_as_int
months = years * 12
weeks = years * 52
days = years * 365

message = f"You have {days} days, {weeks} weeks, and {months} months left until you are 90."
print(message)







