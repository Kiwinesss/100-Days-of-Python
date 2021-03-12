import random
from art import logo
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
print(logo)    
print("Welcome to Blackjack.")
 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
 
 
def draw_card(hand):
    card_index = random.randint(0, len(cards) - 1)
    card = cards[card_index]
    hand.append(card)
 
 
def calculate_score(hand):
    score = sum(hand)
    if len(hand) == 2 and score == 21:
        score = 0
    elif score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score
 
 
def compare(u_score, d_score):
    print(f"Your final hand is: {user_hand}. Your final score is {u_score}.")
    print(f"Computer final hand is: {dealer_hand}. Computer final score is {d_score}.")
 
    if u_score == d_score:
        print("The game is a draw")
    elif u_score > 21:
        print("Bust. You lose")
    elif d_score > 21:
        print("Your opponent went bust. You win!")
    elif u_score == 0:
        print("Blackjack. You win!")
    elif d_score == 0:
        print("Your opponent has a Blackjack. You lose")
    elif u_score > d_score:
        print("You win!")
    else:
        print("You lose")
 
 
def game():
 
    user_score = calculate_score(user_hand)
    dealer_score = calculate_score(dealer_hand)
 
    print(f"Your cards are: {user_hand}. Your current score is {user_score}")
    print(f"The computer's first card is {dealer_hand[0]}")
    if user_score == 0 or dealer_score == 0:
        compare(user_score, dealer_score)
        return
 
    if user_score > 21:
        compare(user_score, dealer_score)
        return
 
    if input("Type 'y' to draw another card. To hold type 'n': ") == "y":
        draw_card(user_hand)
        game()
    else:
        while dealer_score < 17:
            draw_card(dealer_hand)
            dealer_score = calculate_score(dealer_hand)
        compare(user_score, dealer_score)
        return
 
 
while input("Type 'y' if you want to play. Else type 'n': ") == "y":
    cls()
    print(logo)
    user_hand = []
    dealer_hand = []
    while len(user_hand) < 2 and len(dealer_hand) < 2:
        draw_card(user_hand)
        draw_card(dealer_hand)
 
    game()
  
  
  
  
  
  
  
