import art
import random

def deal_card():
    """Returns a random card from the deck which is represented as numbers."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Returns calculated score for the deck as per rules."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_points, computer_points):
    """Decides what to be printed based on the score."""
    if computer_points == 0:
        return "You LOSE!\n - Your opponent has Blackjack 🧐"
    elif user_points == 0:
        return "You WIN!\n - You have a Blackjack 🤫"
    elif user_points > 21:
        return "You LOSE!\n - You busted 🤬"
    elif computer_points > 21:
        return "You WIN!\n - Your opponent busted 😎"
    elif user_points == computer_points:
        return "Draw 🤨\n - The chance of this happening is 8.48%"
    elif user_points > computer_points:
        return "You WIN!\n - You have higher score than your opponent 🤠"
    else:
        return "You LOSE!\n - Your opponent has higher score than you 😩"

def game():
    """This is the base of the blackjack game."""
    user_cards = []
    user_score = 0
    computer_cards = []
    computer_score = 0
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)

        print(f"Your cards: {user_cards}, your score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to get another card or type 'n' to pass: ").lower()
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, your final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, their final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower():
    print("\n" * 20)
    print(art.logo)
    game()