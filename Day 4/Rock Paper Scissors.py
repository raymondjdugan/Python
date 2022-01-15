import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_moves = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)


if player_choice <= (len(game_moves) - 1):
    print("You chose:")
    print(game_moves[player_choice])
    print("\nComputer chose:")
    print(game_moves[computer_choice])

    if player_choice == 0 and computer_choice == 2:
        print("You lose!")
    elif computer_choice == 0 and player_choice == 2:
        print("You win!")
    elif player_choice > computer_choice:
        print("You lose!")
    elif player_choice < computer_choice:
        print("You win!")
    else:
        print("This is a draw!")
else:
    print("This is an invalid choice")






