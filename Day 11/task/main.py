from art import logo
import random as rd

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def show_cards(user_hand, computer_hand, current_score):
    print(f"Your hand: {user_hand}, current score: {current_score}")
    print(f"Computer\'s first card: {computer_hand[0]}")

def check_soft_hand(hand):
    """Checks for aces in the hand and if they need to be changed to a 1 instead of 11"""
    while 11 in hand and sum(hand) > 21:
        index = hand.index(11)
        hand[index] = 1
    return hand

def validate_input(usr_inpt):
    while usr_inpt not in ['y', 'n']:
        usr_inpt = input("Invalid input. Please enter 'y' or 'n': ").lower()
    return usr_inpt

def check_final_score(usr_score, cmptr_score):
    if usr_score > 21:
        print("You went over, you lose!")
    elif cmptr_score > 21:
        print("Opponent went over, you win!")
    elif usr_score > cmptr_score:
        print("You have better cards, you win!")
    elif usr_score < cmptr_score:
        print("Opponent has better cards, you lose!")
    elif usr_score == cmptr_score:
        print("It's a draw!")

def blackjack():
    print(logo)
    user_hand = check_soft_hand(rd.choices(cards, k=2))
    computer_hand = rd.choices(cards, k=2)
    user_score = sum(user_hand)
    show_cards(user_hand, computer_hand, user_score)

    hit_stay = 'y'
    while user_score <= 21 and hit_stay == 'y':
        hit_stay = validate_input(input('Type \'y\' to get another card, or \'n\' to pass: ').lower())
        if hit_stay == 'y':
            user_hand.append(rd.choice(cards))
            check_soft_hand(user_hand)
            user_score = sum(user_hand)
            show_cards(user_hand, computer_hand, user_score)
        else:
            while sum(computer_hand) < 17:
                computer_hand.append(rd.choice(cards))
                check_soft_hand(computer_hand)

    user_score = sum(user_hand)
    computer_score = sum(computer_hand)
    print(f"Your final hand: {user_hand}, final score: {user_score}\n")
    print(f"Computer\'s final hand: {computer_hand}, final score: {computer_score}\n")

    check_final_score(user_score, computer_score)


start_game = 'y'
while start_game == 'y':
    start_game = validate_input(input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': \n').lower())
    if start_game == 'y':
        print("\n" * 20)
        blackjack()
    else:
        print('Ok! Thank you for playing, bye!')
