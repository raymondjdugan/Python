# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
# import random
# import art
#
#
# def number_game():
#     # set a random number between 1 and 100
#     NUMBER_TO_GUESS = random.randint(0, 10)
#     print(f"For testing purposes: Number is {NUMBER_TO_GUESS}")
#
#     # set number of attempts
#     def attempts(user_input):
#         if user_input == 'e':
#             return 10
#         elif user_input == 'h':
#             return 5
#
#     def reduce_attempts():
#         return num_of_attempts - 1
#
#     def guess():
#         return input('Make a guess:')
#
#     game_over = False
#     print(art.logo)
#     print("Welcome to the Number Guessing Game!")
#     print("I am thinking of a number between 1 and 100")
#
#     num_of_attempts = attempts(input("Would you like to play easy or hard mode? Type 'e' or 'he'"))
#     while not game_over:
#         user_number = int(guess())
#
#         if user_number > NUMBER_TO_GUESS:
#             num_of_attempts = reduce_attempts()
#             print("Number is too high")
#             if num_of_attempts != 0:
#                 print('Guess again')
#                 print(f"Attempts remaining: {num_of_attempts}")
#             else:
#                 print("You've run out of guesses, you lose")
#                 game_over = True
#         elif user_number < NUMBER_TO_GUESS:
#             num_of_attempts = reduce_attempts()
#             print("Number is too low")
#             if num_of_attempts != 0:
#                 print('Guess again')
#                 print(f"Attempts remaining: {num_of_attempts}")
#             else:
#                 print("You've run out of guesses, you lose")
#                 game_over = True
#         elif user_number == NUMBER_TO_GUESS:
#             game_over = True
#             print(f"You got it! The answer was {NUMBER_TO_GUESS}")
#
#
# while input("Would you like to play again? 'y' or 'n'") == 'y':
#     number_game()

logo = """
┌∩┐(◕_◕) ┌∩┐
"""

print(logo)