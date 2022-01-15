# 🚨 Don't change the code below 👇
height = float(input("Enter your height in feet: "))
weight = float(input("enter your weight in pounds: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round(703 * weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}%, you are underweight.")
elif bmi < 22:
    print(f"Your BMI is {bmi}%, you have a normal weight.")
elif bmi < 28:
    print(f"Your BMI is {bmi}%, you are slightly overweight.")
elif bmi < 33:
    print(f"Your BMI is {bmi}%, you are obese.")
else:
    print(f"Your BMI is {bmi}%, you are clinically obese.")