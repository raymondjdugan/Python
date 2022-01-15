# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_height = 0
length_of_list = 0

avg = int
for num in student_heights:
    total_height += num
    length_of_list += 1
    avg = round(total_height / length_of_list)

print(avg)
