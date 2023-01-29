suits = ['C', 'H', 'D', 'S']
cards = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
]
full_deck = []
for suit in suits:
    for card in cards:
        full_deck.append(suit + card)
print(full_deck)

