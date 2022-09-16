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

#
# # Square Numbers Challenge
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
# squared_numbers = [num**2 for num in numbers]


# #Write your code 👆 above:
#
# print(squared_numbers)
#
# # Challenge 3
# # with open("file1.txt") as file1:
# #     file_one_nums = file1.readlines()
# # with open("file2.txt") as file2:
# #     file_two_nums = file2.readlines()
# #
# # result = [int(num) for num in file_one_nums if num in file_two_nums]
# #
# # # Write your code above 👆
# #
# # print(result)


# Dictionary Comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# scores = {student: random.randint(1, 100) for student in names}
# print(scores)
#
# passed_students = {student: score for (student, score) in scores.items() if score >= 60}
# print(passed_students)

# Dictionary Comprehension Coding Challenge 1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
# result = {word: len(word) for word in sentence.split()}
# # Write your code below:
#
# print(result)

