import random
# list1 = [1,5,1,8,5]
# list2 = [2,8,0]
#
# ratio = (len(list2)/len(list1))*100
# print(round(ratio))
#
# # for i in list1:
# #     print(i)
# print(len(list1))
# list1.pop(0)
# print(list1[0])
# print(len(list1))
# print()
# print()
# print()
#
# list2 = [{'a': [{'i': 'p'}, {'ii': 'pp'}, {'iii': 'ppp'}]}, {'b': [{'iiii': 'pppp'}, {'iiiii': 'ppppp'}]}]
# for index in list2:
#     print(index)
#     for i in index:
#         print(i)
#         for p in i:
#             for x in p:
#                 print(x)

# word = 'Python'
# print(word[::-1])

# list1 = {'John': [{'value': 1}, {'value': 2}], 'John2': [{'value': 3, 'sign': 's'}, {'value': 7, 'sign': 'k'}]}
# print(list1)
# list1['John'].append({'value': 1, 'sign': 2})
# print(list1)

list2 = {'username': [{'va'}]}

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
signs = ['H', 'D', 'C', 'S']

cardValues = [
    {'2': 2},
    {'3': 3},
    {'4': 4},
    {'5': 5},
    {'6': 6},
    {'7': 7},
    {'8': 8},
    {'9': 9},
    {'10', 10},
    {'J': 10},
    {'K': 10},
    {'Q': 10},
    {'A': 11}
]

deck = [{'value': value, 'sign': sign} for value in values for sign in signs]
print(deck)
random.shuffle(deck)
print(deck[0])
# cardsInPlay = {}
# print(deck)
# x = 0
# while x < 1:
#
#     print(deck[0])
#     cardsInPlay.append('player', deck[0])
#     deck.pop(0)
#     x = x+1
#
# y = 0
# while y < 2:
#     print(deck[0])
#     cardsInPlay.update(deck[0])
#     deck.pop(0)
#     y = y+1
# print(deck)
# print(cardsInPlay)

print()
print()
print()
print()

list1 = {'John': [{'value': 1}, {'value': 2}], 'John2': [{'value': '3', 'sign': 's'}, {'value': '7', 'sign': 'k'}]}
print(list1)
list1['John'].append({'value': 1, 'sign': 2})
print(list1)
list1['John'].append({'value': 45, 'sign': 'S'})
print(list1)
list1['John2'].append(deck[0])
print(list1)

print()
print('-----------------')
print()
print(list1['John2'])
print()
print(len(list1['John2']))
print('----------------------')
print(list1['John2'])
print()
print()
for card in list1['John2']:
    print(card)
    print(card['value'])

print()
print('-----------------')
print()
for values in cardValues:
    print(values)
    for val in values:
        print(val)
        if val == '2':
            print('--------')
            print(val)
            print('--------')


list3 = {}
list3.update({'player': []})
print(list3)
list3['player'].append({'val': 2, 'sign': 's'})
print(list3)
list3['player'].append({'val': 2, 'sign': 's'})
print(list3)
list3['player'].append({'val': 2, 'sign': 's'})
print(list3)
list3.update({'GOD': []})
print(list3)
list3['GOD'].append({'val': 6, 'sign': 'h'})
print(list3)
list3['GOD'].append(deck[0])
print(list3)
print(deck[0])
print(len(deck))
deck.pop(0)
print(len(deck))
print(list3)
print()
print()
print()
print('-------------------------')

numberOfDeck = 3
# deckTwo = [{'value': value, 'sign': sign} for value in values for sign in signs]
deckTwo = []
i = 0
while i < numberOfDeck:
    for element in deck:
        deckTwo.append(element)

    i = i+1


# print(deckTwo)
# print(len(deckTwo))
#
# print(list1['John2'])
# for card in list1['John2']:
#     # print(card['value'])
#     for value in cardValues:
#         print(value)
#         print()
#         print(card['value'])
#         for val in value:
#             # print('***********')
#             # print(val)
#             # print('**************')
#             if card['value'] == val:
#                 print('--------------')
#                 print(card['value'], val)
#                 print('--------------')
# print()
# print(list1)
print()
for card in list1['John2']:
    playerCard = card['value']
    # print(playerCard)
    for values in cardValues:
        for val in values:
            if playerCard == val:
                print('----START----')
                # print(playerCard, ' - ', val)
                print(values[playerCard])
                print('----END----')
        # print(values[playerCard])
print(cardValues)
