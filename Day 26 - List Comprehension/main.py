# List Comprehension
# new_list = [new_item for item in list]
# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)
#
# # Range List
# range_list = [num * 2 for num in range(1, 5)]
# print(range_list)
#
# Conditional List Comprehension
# new_list = [new_item for item in list if test]
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) <=4]
# print(short_names)
#
# upper_names = [name.upper() for name in names if len(name) > 5]
# print(upper_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:
squared_numbers = [pow(num, 2) for num in numbers]


#Write your code 👆 above:

print(squared_numbers)
