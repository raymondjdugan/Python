# Functions with return
# def my_function():
#   result = 3 * 2
#   return result
#         #or
#   return 3 * 2

# def format_name(f_name, l_name):
#   formatted_f_name = f_name.title()
#   formatted_l_name = l_name.title()
#   return f"{formatted_f_name} {formatted_l_name}"
#   #the return is the end of the function
# print(format_name("ray", "dugan"))


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
    # the return is the end of the function


print(format_name(input("What is your first name?\n"), input("What is your last name?\n")))
