import random
import os

deck = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
signs = ['H', 'D', 'C', 'S']

minPlayers = 2
maxPlayers = 7
# make deck with list comprehension
# deck = [i for i in {'value': values, 'sign': signs}]

print(deck)

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
        for x in range(2):
            print('Lenght01:', len(deck))
            for i in range(int(playerNo)):
                maxDeckIndex = len(deck)-1
                randCard = random.randint(0, maxDeckIndex)
                print('Lenght:', len(deck))
                print('Pop:', randCard)
                print(deck[randCard])
                cardsInPlay.append([i, deck[randCard]])
                deck.pop(randCard)
                print(randCard)
            print(cardsInPlay)

        for card in cardsInPlay:
            print(card)
            for index in card:
                print('INDEX: ', index)

        # for x in range(len(deck)):
        #     print(deck[x])
        # break



