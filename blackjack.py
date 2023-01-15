import random
import os
from typing import List, Any

# deck = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
signs = ['H', 'D', 'C', 'S']
minPlayers = 2
maxPlayers = 7


def drawCard(deck_name, player_number):
    max_deck_index = len(deck_name) - 1
    print(max_deck_index)
    rand_card = random.randint(0, max_deck_index)
    cardsInPlay.append([player_number, deck[rand_card]])
    deck.pop(rand_card)
    return cardsInPlay


# make deck with list comprehension
# deck = [i for i in {'value': values, 'sign': signs}]

# for value in values:
#     for sign in signs:
#         deck.append({'value': value, 'sign': sign})
#
# # print(deck)
# for x in range(len(deck)):
#     print(deck[x])

deck = [[{'value': value, 'sign': sign}] for value in values for sign in signs]
for x in range(len(deck)):
    print(deck[x])

newRound = True
while newRound:
    playerNo = input('How many people are playing? : ')

    cardsInPlay = []

    # Number of players is between the MAX and MIN values
    while playerNo.isnumeric() and maxPlayers >= int(playerNo) >= minPlayers:

        # rand = random.randint(0, len(deck))
        # print(rand)

        # deck.pop(rand)
        # for x in range(len(deck)):
        #     print(deck[x])

        # if there is less then 2 cards left, error, please fix !!

        for player in range(0, int(playerNo)):
            # drawCard(deck, int(playerNo))
            # print(deck)
            if player <= int(playerNo):
                drawCard(deck, player)
                for card in cardsInPlay:
                    for index in card:
                        print('INDEX: ', index)
                        if index == player:
                            print('Pass: ', card)
            print(cardsInPlay)
            stop = input('Stop here for a moment')
        # for x in range(len(deck)):
        #     print(deck[x])
        # break



