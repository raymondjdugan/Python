# For Loop
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# For loops with range()
num: int
# range(start, stop, step)
for num in range(1, 11, 3):
    print(num)

total = 0
for number in range(1, 101):
    total += number
print(total)
