import random
import csv
import os
# leaderboard, write into a new file
# at the start is a menu (startgame, leaderboard)
# save cards into a dictionary
# shuffle is a function in python to shuffle the dictionary
# always take the 0. card
# do not use random choice, but radnom shuffle instead (the dictionary)


# Function to get back to the main menu
def goBack(at_menu, at_place):
    wrong_input = True
    while wrong_input:
        go_back = input('Return back: [press enter]')
        if go_back == '':
            at_menu = True
            at_place = False
            wrong_input = False
    return at_menu, at_place


def totalValue(cards_values, players_cards, player_name):
    total_card_value = 0
    has_ace = False

    for current_card in players_cards[player_name]:
        player_card = current_card['value']
        for vals in cards_values:
            for val in vals:
                if player_card == val:
                    # print(vals[player_card])
                    total_card_value = total_card_value + vals[player_card]
        # Searches for an ace
        if player_card == 'A':
            has_ace = True

    # If the value exceeds 21, check for ace and assign correct value
    if total_card_value > 21 and has_ace:
        total_card_value = total_card_value-10
    return total_card_value


def drawCard(deck_name, player_name):
    current_card = deck_name[0]
    playerCards[player_name].append(current_card)
    deck_name.pop(0)
    return playerCards


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
signs = ['H', 'D', 'C', 'S']

cardsValues = [
    {'2': 2},
    {'3': 3},
    {'4': 4},
    {'5': 5},
    {'6': 6},
    {'7': 7},
    {'8': 8},
    {'9': 9},
    {'10': 10},
    {'J': 10},
    {'K': 10},
    {'Q': 10},
    {'A': 11}
]

chipsVal = [1, 5, 25, 100, 500, 1000]
startChips = 100    # dollars
playerChips = {}
playerBets = {}

stats = []

minPlayers = 1
maxPlayers = 7
dealer = 'The Dealer'

decksAmount = 0

playerNames = []

playerCards = {}

deckTemplate = [{'value': value, 'sign': sign} for value in values for sign in signs]
deck = []

programRunning = True
atMenu = True
inGame = False
atLeaderBoard = False
atRules = False
samePlayers = False

print('Blackjack')
print()

while programRunning:
    # os.system('cls')
    print()
    print('Start the game [0]')
    print('Leaderboard [1]')
    print('Rules [2]')
    print('Quit [3]')

    while atMenu:
        menuOption = input('Your option: ')

        if menuOption.isnumeric():
            if int(menuOption) == 0:
                print('The game is starting...')
                atMenu = False
                inGame = True
            elif int(menuOption) == 1:
                print('Loading the leaderboard...')
                atMenu = False
                atLeaderBoard = True
            elif int(menuOption) == 2:
                print('Loading the rules...')
                atMenu = False
                atRules = True
            elif int(menuOption) == 3:
                print('Closing the game...')
                programRunning = False
                break
            else:   # invalid number value
                atMenu = True
        else:   # option is not a number
            atMenu = True

    while atLeaderBoard:
        # os.system('cls')
        print('Here is the leaderboard!')

        # at the end use can choose to go back to the main menu
        atMenu, atLeaderBoard = goBack(atMenu, atLeaderBoard)

    while inGame:
        # os.system('cls')
        invalidDecksAmount = True
        deletePlayers = False
        inRound = True

        if len(playerNames) != 0:
            newPlayers = input('Do you want to delete all players? [Y/N]: ')
            if newPlayers.lower() == 'y':
                playerNames = []
            elif newPlayers.lower() == 'n':
                samePlayers = True
                print('This game will be played with following players: ')
                for username in playerNames:
                    print(username)

        print('Start')

        while invalidDecksAmount:
            if decksAmount != 0:
                newAmount = input('Play with different amount of decks? [Y/N]: ')
                if newAmount.lower() == 'y':
                    decksAmount = input('How many decks do you want to use? [1-8]: ')
                    if decksAmount.isnumeric():
                        if 1 <= int(decksAmount) <= 8:
                            print('The game will be played with ', decksAmount, ' deck(s)')
                            invalidDecksAmount = False
                        else:   # Selected deck amount is invalid
                            print('Invalid amount of decks')
                            decksAmount = 0
                    else:
                        decksAmount = 0
                elif newAmount.lower() == 'n':
                    print('The game will be played with ', decksAmount, ' deck(s)')
                    invalidDecksAmount = False
            else:   # Deck amount wasn't selected yet
                decksAmount = input('How many decks do you want to use? [1-8]: ')
                if decksAmount.isnumeric():
                    if 1 <= int(decksAmount) <= 8:
                        print('The game will be played with ', decksAmount, ' deck(s)')
                        invalidDecksAmount = False
                    else:
                        print('Invalid amount of decks')
                        decksAmount = 0
                else:
                    decksAmount = 0

        # print(len(deck))
        inAddPlayer = True

        while inAddPlayer:

            if not samePlayers:
                print('Create the player accounts.')
                addplayer = True
            else:
                addplayer = False
                inAddPlayer = False
            while addplayer:
                invalidInput = True
                player = input('Write your username, please: ')

                if len(player.strip()) == 0:
                    addplayer = True
                else:
                    invalidInput = True
                    if playerNames.count(player) != 0 or player == dealer:
                        invalidInput = False
                    else:
                        playerNames.append(player)

                        print('Player has been added')
                        print('Current number of players is: ', len(playerNames))
                        while invalidInput:
                            invalidInput = False
                            anotherPlayer = input('Do you want to add another player? [Y/N]: ')
                            if anotherPlayer.lower() == 'y':
                                addplayer = True
                            elif anotherPlayer.lower() == 'n':
                                addplayer = False
                                inAddPlayer = False
                            else:
                                invalidInput = True
        roundNo = 1
        while inRound:
            # Keeps count of the while loop, must be less then amount of decks appended
            i = 0
            while i < int(decksAmount):
                # Loops over all elements in the deck template and appends them to the deck
                for element in deckTemplate:
                    deck.append(element)
                i = i + 1
            playerCards.update({dealer: []})
            random.shuffle(deck)
            print('The round is starting')
            # Adds the dealer into the list of users with cards in play
            for player in playerNames:
                playerCards.update({player: []})
                if roundNo == 1:
                    playerChips.update({player: 100})
                print(playerCards)

            for i in range(2):
                for player in playerNames:
                    playerCards = drawCard(deck, player)
                playerCards = drawCard(deck, dealer)
            # print(playerNames)
            print(playerChips)
            print(playerCards)
            print('Place your bets!')
            for player in playerNames:
                print('-------------------------------')
                print('Player: ', player)
                print('You have: ', playerChips[player], ' coins')
                invalidInput = True
                while invalidInput:
                    bet = input('Your bet: ')
                    if bet.isnumeric():
                        if 0 < int(bet) <= playerChips[player]:
                            playerBets.update({player: int(bet)})
                            playerChips[player] = playerChips[player] - int(bet)
                            invalidInput = False
            print(playerChips)
            for player in playerNames:
                wrongInput = True
                print('-------------------------------')
                print('PLAYER: ', player)
                print('Total: ', totalValue(cardsValues, playerCards, player))
                if totalValue(cardsValues, playerCards, player) == 21:
                    print('Blackjack! Wait for the results')
                    wrongInput = False
                print('Turn of: ', player)
                while wrongInput:
                    wrongInput = False
                    choice = input('Do you choose to Stand or Hit? [S/H]: ')
                    if choice.lower() == 's':
                        print('You chose to stand.')
                    elif choice.lower() == 'h':
                        print('You chose to hit')
                        wrongInput = True
                        playerCards = drawCard(deck, player)
                        print(totalValue(cardsValues, playerCards, player))
                        if totalValue(cardsValues, playerCards, player) > 21:
                            coins = playerBets[player]
                            print('You went bust and lost: ', coins, ' coins')
                            wrongInput = False
                        elif totalValue(cardsValues, playerCards, player) == 21:
                            print('21! Wait for the game results.')
                            wrongInput = False
                    else:
                        wrongInput = True
            pause = input('continue [enter]')
            print('The Dealer: ')
            dealer_total = totalValue(cardsValues, playerCards, dealer)
            print('Total: ', dealer_total)
            for cards in playerCards[dealer]:
                print()
                # print(cards)
                # print(cards['value'])
            while dealer_total < 17:
                playerCards = drawCard(deck, dealer)
                dealer_total = totalValue(cardsValues, playerCards, dealer)
                # print(playerCards[dealer])
            for player in playerNames:
                print('--------------------')
                print(player)
                total = totalValue(cardsValues, playerCards, player)
                coins = playerBets[player]
                print('Total: ', total)
                print('Bet: ', coins, ' coins')
                if dealer_total > 21:
                    print()
                    print('Dealers new total', dealer_total)
                    print('The dealer went bust! ')
                    if total == 21 and len(playerCards[player]) == 2:
                        playerChips[player] = coins + ((3 / 2) * coins)
                    if total < 21 or (total == 21 and len(playerCards[player]) != 2):
                        playerChips[player] = playerChips[player] + 2*coins
                        print(playerChips[player])

                elif dealer_total == 21:
                    if len(playerCards[dealer]) == 2:
                        print('The dealer has blackjack!')
                    else:
                        print('The dealer won!')

                    if total == dealer_total:
                        playerChips[player] = playerChips[player] + coins
                        print('It is a drew!')
                    elif total < dealer_total:
                        print('You lost!')

                else:   # Dealers total is less then 21
                    if total == 21 and len(playerCards[player]) == 2:
                        playerChips[player] = playerChips[player] + ((3 / 2) * coins)
                        print('Add', playerChips[player])
                    elif dealer_total < total < 21 or (total == 21 and len(playerCards[player]) != 2):
                        playerChips[player] = playerChips[player] + 2 * coins
                        print(playerChips[player])
                    elif dealer_total == total:
                        playerChips[player] = playerChips[player] + coins

            for player in playerNames:
                print('-------------------')
                print('Player: ', player)
                print('Coins left: ', playerChips[player])
                stats.append(playerChips[player])
                if playerChips[player] == 0:
                    playerNames.remove(player)

            with open('leaderboard.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerow(stats)

            # at the end use can choose to go back to the main menu or play another round
            firstRound = False
            playAgain = True
            while playAgain:
                again = input('Play another round? [Y/N]: ')
                if again.lower() == 'y':
                    roundNo = roundNo + 1
                    inRound = True
                    playAgain = False
                elif again.lower() == 'n':
                    inRound = False
                    atMenu, inGame = goBack(atMenu, inGame)

    while atRules:
        # os.system('cls')
        print('The Rules of The Game of Blackjack')
        print('Rule No.1: ')

        atMenu, atRules = goBack(atMenu, atRules)
