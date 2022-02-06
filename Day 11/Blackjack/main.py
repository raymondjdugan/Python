############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################
import random
import art
# from replit import clear


def blackjack():
    print(art.logo)

    # Function to deal cards
    def deal_card():
        """Returns a random card from the deck"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    # Function to get the total of the cards
    def calc_cards(cards):
        """Take a list of cards and return the total of the list"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0

        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    def compare(dealer, player):
        if dealer == player:
            return 'Game is a draw.'
        elif dealer == 0:
            return "Dealer has blackjack."
        elif player == 0:
            return "Player has blackjack. Winner, Winner, Chicken Dinner!"
        elif dealer > 21:
            return f"Player wins with {player}."
        elif player > 21:
            return f"Dealer wins!"
        elif dealer < player:
            return f"Player wins with {player}."
        else:
            return f"Dealer wins!"

    # Creating empty card lists
    player_cards = []
    dealer_cards = []
    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        dealer_total = calc_cards(dealer_cards)
        print(f" Dealer's first card is {dealer_cards[0]}")
        player_total = calc_cards(player_cards)
        print(f" Player's cards are {player_cards}, Current Score: {player_total}\n")

        if dealer_total == 0 or player_total == 0 or player_total > 21:
            is_game_over = True
        else:
            user_choice = input("Would you like to card or hold? Enter 'c' for card and 'h' for hold.\n")
            if user_choice == 'c':
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while dealer_total != 0 and dealer_total < 17:
        dealer_cards.append(deal_card())
        dealer_total = calc_cards(dealer_cards)

    if player_total == 0:
        print(f" Your final hand: {player_cards}, Final score: 21")
    else:
        print(f" Your final hand: {player_cards}, Final score: {player_total}")

    if dealer_total == 0:
        print(f" Dealer final hand: {dealer_cards}, Final score: 21")
    else:
        print(f" Dealer final hand: {dealer_cards}, Final score: {dealer_total}")

    print(compare(dealer_total, player_total) + '\n')


while input("Do you want to play the again? Type 'y' for yes and 'n' for no") == 'y':
    # clear()
    blackjack()
