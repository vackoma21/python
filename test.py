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

list1 = {'John': [{'value': 1}, {'value': 2}], 'John2': [{'value': 3, 'sign': 's'}, {'value': 7, 'sign': 'k'}]}
print(list1)
list1['John'].append({'value': 1, 'sign': 2})
print(list1)

list2 = {'username': [{'va'}]}

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
signs = ['H', 'D', 'C', 'S']

deck = [{'value': value, 'sign': sign} for value in values for sign in signs]

random.shuffle(deck)
cardsInPlay = {}
print(deck)
x = 0
while x < 1:

    print(deck[0])
    cardsInPlay.update({'player': deck[0]})
    deck.pop(0)
    x = x+1

y = 0
while y < 2:
    print(deck[0])
    cardsInPlay.update(deck[0])
    deck.pop(0)
    y = y+1
print(deck)
print(cardsInPlay)
