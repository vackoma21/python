import random
import os

# fiks (na cvut vysoka ukoly)
# deck = []

# double down, po rozdani karet, moznost zahrat double down (napr 4, 5),
# zdvojnasobi se sazka a uz nehraje (pri napr 10, 11 soucet)
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
signs = ['H', 'D', 'C', 'S']

chipsVal = [1, 5, 25, 100, 500, 1000]

minPlayers = 1
maxPlayers = 7


def drawCard(deck_name, player_number):
    max_deck_index = len(deck_name) - 1
    # print(max_deck_index)
    rand_card = random.randint(0, max_deck_index)
    cardsInPlay.append([player_number, deck[rand_card]])
    deck.pop(rand_card)
    return cardsInPlay


def betting():
    bet = input('Place your bet, must be made out of existing chips [1, 5, 25, 100, 500, 1000]: ')
    for chip in chipsVal:
        if bet % chip == 0:
            return bet
    return False


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
        player = 0
        for player in range(0, int(playerNo)):
            # drawCard(deck, int(playerNo))
            # print(deck)
            print('NEW ROUND')
            print()
            print(cardsInPlay)
            print()
            print('PLAYER: ', player)
            drawCard(deck, player)
            for card in cardsInPlay:
                for index in card:
                    print('INDEX: ', index)
                    if index == player:
                        print('Pass: ', card)
                print('NEW LINE')
        # print(cardsInPlay)
        stop = input('Stop here for a moment')
        print('SECOND PLAYER')
        print()
        print()
        print(cardsInPlay)
        print()
        # for x in range(len(deck)):
        #     print(deck[x])
        # break



