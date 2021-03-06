# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the Tip Calculator\n")

# Getting the bill amount, tip amount and the number of the party
bill = input("What was your final bill?\n")
tip = input("How much would you like to give? 10, 12, or 15\n")
ppl = input("How many people will split the bill?\n")

# Converting string to float and int
billAsFloat = float(bill)
tipAsFloat = float(tip) / 100 + 1
pplAsInt = int(ppl)

# Calculating the final bill
finalBill = round((billAsFloat / pplAsInt) * tipAsFloat, 2)

# Constructing and printing the final bill mesage
message = f"Each person should pay ${float(finalBill)}."
print(message)
