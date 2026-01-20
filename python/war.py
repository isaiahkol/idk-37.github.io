"""
Final Project: War (Card Game)
Isaiah Kol
CS 1210-D
"""

import random
import os

SUITS = ['♥', '♣', '♦', '♠']
RANKS = {'A':13, 'K':12, 'Q':11, 'J':10, '10':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}

def card_image(rank, suit):
    top = "◤————————◥"
    bottom = "◣————————◢"
    if len(rank) == 1:
        middle_1 = (f"|{rank}        |")
    elif len(rank) == 2:
        middle_1 = (f"|{rank}       |")
    middle_2 = ("|         |")
    middle_3 = (f"|    {suit}    |")
    middle_4 = ("|         |")
    if len(rank) == 1:
        middle_5 = (f"|        {rank}|")
    elif len(rank) == 2:
        middle_5 = (f"|       {rank}|")
    return [top, middle_1, middle_2, middle_3, middle_4, middle_5, bottom]

def adj_cards(card_1, card_2):
    p_card = card_image(card_1[0], card_1[1])
    c_card = card_image(card_2[0], card_2[1])
    print("Player:\t\tComputer:")
    for line in range(7):
        print(p_card[line] + "\t" + c_card[line])

def make_deck(ranks, suits):
    deck = []
    for rank in ranks:
        for suit in suits:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def split_deck(deck):
    p_deck = []
    c_deck = []
    n = 1
    for card in deck:
        if n % 2 != 0:
            p_deck.append(card)
        else:
            c_deck.append(card)
        n += 1
    return (p_deck, c_deck)

def turn(player_card, computer_card):
    p_card_val = RANKS[player_card[0]]
    c_card_val = RANKS[computer_card[0]]
    if p_card_val > c_card_val:
        return "player"
    elif p_card_val < c_card_val:
        return "computer"
    else:
        return "war"

def war(p_deck, c_deck, in_play):
    if len(p_deck) <= 3:
        return "computer"
    if len(c_deck) <= 3:
        return "player"
    for card in range(3):
        in_play.append(p_deck.pop())
        in_play.append(c_deck.pop())
    p_war_card = p_deck.pop()
    c_war_card = c_deck.pop()
    in_play.append(p_war_card)
    in_play.append(c_war_card)
    print("\nWAR!\n")
    adj_cards(p_war_card, c_war_card)
    for card in range(3):
        print("⌊_________⌋\t⌊_________⌋")
    return turn(p_war_card, c_war_card)

def play_war(p_deck, c_deck, round_lim):
    round_num = 0
    print("\nWELCOME TO WAR!\n")
    while p_deck and c_deck and (round_lim == -1 or round_num < round_lim):
        input("Hit ENTER to play a card:")
        round_num += 1
        os.system("cls")
        print(f"\nROUND {round_num} \n")
        print(f"Player Cards Remaining: {len(p_deck)}\n"
              f"Computer Cards Remaining: {len(c_deck)}\n")
        in_play = []
        p_card = p_deck.pop()
        c_card = c_deck.pop()
        in_play += [p_card, c_card]
        adj_cards(p_card, c_card)
        result = turn(p_card, c_card)
        while result == 'war':
            result = war(p_deck, c_deck, in_play)
        if result == 'player':
            print(f"\nYOU WIN ROUND {round_num}!")
            for card in in_play:
                p_deck.insert(0, card)
        elif result == 'computer':
            print(f"\nCOMPUTER WINS ROUND {round_num}!")
            for card in in_play:    
                c_deck.insert(0, card)
        if round_lim != -1:
            print(f"{round_lim - round_num} ROUNDS REMAINING!")
    if round_lim == round_num:
        if len(p_deck) > len(c_deck):
            print("\nYOU WIN THE WAR!\nYou had more cards than "
                  "the computer at the round limit. Try a full game?")
        elif len(p_deck) < len(c_deck):
            print("\nCOMPUTER WINS THE WAR!\nThe computer had more cards "
                  "than you at the round limit. Try a full game?")
        else:
            print("\nIT'S A TIE! You and the computer had an equal "
                  "card count at the round limit. Try a full game?")
    elif p_deck:
        print("\nYOU WIN THE WAR!\nGood job. Very War.")
    elif c_deck:
        print("\nCOMPUTER WINS THE WAR!\nWomp Womp.")

if __name__ == "__main__":
    os.system("cls")
    while True:
        try:
            rounds = input("How many rounds of WAR would you like to play?\n"
                      "Enter a positive integer, or 'f' for full game: ")
            if rounds == "f":
                round_lim = -1
                break
            if int(rounds) <= 0:
                print("Please enter a POSITIVE integer.")
            else:
                round_lim = int(rounds)
                break
        except ValueError:
            print("Error. Try again.")

    deck = make_deck(RANKS.keys(), SUITS)
    (p_deck, c_deck) = split_deck(deck)
    play_war(p_deck, c_deck, round_lim)

