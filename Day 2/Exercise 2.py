# 🚨 Don't change the code below 👇
height = input("Enter your height in feet: ")
weight = input("Enter your weight in pounds: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = 703 * float(weight) / (float(height) ** 2)
bmi_as_int = int(bmi)

print(f"You're BMI is {bmi_as_int}%")

