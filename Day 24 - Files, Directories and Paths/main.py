# Read Only Mode
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Write mode - If the file does not exist, it will create the file.
with open("my_file.txt", mode="w") as file:
    file.write("new text")

# Append Mode
with open("my_file.txt", mode="a") as file:
    file.write("new text")