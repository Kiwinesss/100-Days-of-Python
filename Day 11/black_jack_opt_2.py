import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
from art import logo
import random
 
def deal_cards():
  ''' This fucntion deals one card when called from the list "cards"'''
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card_value = random.choice(cards)
  return card_value
 
def calculate_score(cards):
  '''Calculates the total score and checks for a blackjack'''
  if sum(cards) == 21 and len(cards) == 2:
    return 21
  elif 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
    return sum(cards)
  else:
    return sum(cards)
 
def compare_resluts(player_total, dealer_total):
  '''Compares the players cards to the dealers cards and returns the results of the hand'''
  final_result = ""
  if player_total > 21:
    final_result = (f"Your cards: {p_cards}!\nYou Bust!\nYou got {player_total} You Lose!")
  elif dealer_total >21:
    final_result = (f"Dealer cards: {d_cards}!\nDealer Busts!\nDealer got {dealer_total}.\nYou got {player_total}.\nYou Win!")
  elif player_total > dealer_total:
    final_result = (f"Your hand is {player_total}\nDealer cards: {d_cards}.\nDealer's hand is {dealer_total}.\nYou Win!")
  elif player_total == dealer_total:
    final_result = (f"Your cards: {p_cards}! Your hand is {player_total}\nDealer cards: {d_cards}.\nDealer's hand is {dealer_total}.\nIt's a draw!")
  else:
    final_result = (f"Your Card: {p_cards}.\nYour hand is {player_total}\nDealer cards: {d_cards}.\nDealer's hand is {dealer_total}.\nDealer Wins!")
  return final_result
 
def dealer_hand(dealer_cards):
  '''plays the dealer's side of the game. Logic for the dealer hitting or standing.  Returns dealer's cards and dealer's card total.'''
  dealer_cards_total = calculate_score(dealer_cards)
  while sum(dealer_cards) < 17:
    print()
    dealer_cards.append(deal_cards())
    dealer_cards_total = calculate_score(dealer_cards)
    print(f"Dealer hits. Dealer cards: {dealer_cards}")
  return dealer_cards, dealer_cards_total
 
def player_hand(player_cards):
  '''Logic for the player hitting or standing.  Returns player's cards and player's card total.'''
  player_cards_total = calculate_score(player_cards)
  hit="y"
  if player_cards_total == 21 and len(player_cards) == 2:
    blackjack = True
    return player_cards, player_cards_total, blackjack
  else:
    blackjack = False
  print(f"Your cards: {player_cards}, current score: {player_cards_total}")
  print(f"Dealer's first card: {d_cards[0]}")
  hit = input("Type 'y' to get another card, type 'n' to pass: ")
  if hit == "y":
    while hit == "y":
      player_cards.append(deal_cards())
      player_cards_total = calculate_score(player_cards)
      if player_cards_total > 21:
        hit = "n"
      else:
        print(f"Your cards: {player_cards}, current score: {player_cards_total}")
        print(f"Dealer's first card: {d_cards[0]}")
        hit = input("Type 'y' to get another card, type 'n' to pass: ")
  return player_cards, player_cards_total, blackjack
def check_for_blackjack(cards):
  '''Checks dealers cards for a blackjack.  Returns True and moves to the compare score if it finds one.  US rules if the dealer has a BJ and the player has a BJ, then it's a push'''
  if sum(cards) == 21 and len(cards) == 2:
    return True
 
def play_game(p_cards, d_cards, p_cards_total, d_cards_total, continue_playing):
  '''Logic for the playing the game.  Will call the other functions.'''
  d_blackjack = check_for_blackjack(d_cards)
  if d_blackjack == True:
    final_resluts = compare_resluts(p_cards_total, d_cards_total)
    print(final_resluts)
    continue_playing = input("Would you like to play again? (y/n): ").lower()
    if continue_playing == "y":
      return True
    else:
      return False
 
  while continue_playing == 'y':
    clear()
    print(logo)
 
    p_cards, p_cards_total, p_blackjack = player_hand(p_cards)
 
    print(f"Your cards: {p_cards}, current score: {p_cards_total}")
    print(f"Dealers's first card: {d_cards[0]}")
    
    if p_cards_total <= 21 and p_blackjack == False:
      d_cards, d_cards_total = dealer_hand(d_cards)
    elif p_blackjack == True:
      final_resluts = compare_resluts(p_cards_total, d_cards_total)
 
    final_resluts = compare_resluts(p_cards_total, d_cards_total)
    print(final_resluts)
    continue_playing = input("Would you like to play again? (y/n): ").lower()
    if continue_playing == "y":
      return True
    else:
      return False
 
 
is_game_active = True
clear()
print(logo)
play_the_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
if play_the_game != "y":
  is_game_active = False
 
while is_game_active == True:
  cls()
  print(logo)
  p_cards = [deal_cards(),deal_cards()]
  d_cards = [deal_cards(),deal_cards()]
  d_cards_total = sum(d_cards)
  p_cards_total = sum(p_cards)
  is_game_active = play_game(p_cards, d_cards, p_cards_total, d_cards_total, play_the_game)
clear()
print(logo)
print("Thanks for playing!")
