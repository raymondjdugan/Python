from art import logo, vs
from game_data import data
import random


def get_random_acc():
    return random.choice(data)


def format_data(account):
    return f"{account['name']}, {account['description']}, from {account['country']}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    high_score = 0
    playing = True
    account_a = get_random_acc()
    account_b = get_random_acc()

    while playing:
        account_a = account_b
        account_b = get_random_acc()

        while account_a == account_b:
            account_b = get_random_acc()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_answer(guess, account_a["follower_count"], account_b["follower_count"])

        print(logo)
        if is_correct:
            high_score += 1
            print(f"You're right! Current score: {high_score}.")
        else:
            playing = False
            print(f"Sorry, that's wrong. Final score: {high_score}")


game()

