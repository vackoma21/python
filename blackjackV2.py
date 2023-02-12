import random
import csv
# leaderboard, write into a new file
# at the start is a menu (startgame, leaderboard)
# save cards into a dictionary
# shuffle is a function in python to shuffle the dictionary
# always take the 0. card
# do not use random choice, but random shuffle instead (the dictionary)


# Function to get back to the main menu
# at_menu = bool value for being in menu
# at_place = bool value for being at option places that you go to from the menu
def goBack(at_menu, at_place):
    wrong_input = True
    # If the user doesn't press enter, it will ask they to do so until they do
    while wrong_input:
        go_back = input('Return back: [press enter]')
        if go_back == '':
            at_menu = True
            at_place = False
            wrong_input = False
    # Returns correct boolean values for variables to get to main menu
    return at_menu, at_place


# Returns total value of players/dealers hand, has solution for ace
# cards_value = a dictionary with card values and point values of all cards
# players_cards = a dictionary of all players (+ dealer) and their cards
# player_name = name of the player/dealer
def totalValue(cards_values, players_cards, player_name):
    total_card_value = 0
    # sets default state for existence of ace in players/dealers hand
    has_ace = False
    
    # For every card in players hand find value and match it with values in card_values
    for current_card in players_cards[player_name]:
        player_card = current_card['value']
        for vals in cards_values:
            for val in vals:
                if player_card == val:
                    # print(vals[player_card])
                    # Adds up all found values into one variable
                    total_card_value = total_card_value + vals[player_card]
        # Searches for an ace
        if player_card == 'A':
            has_ace = True

    # If the value exceeds 21, check for an ace and assign correct value
    if total_card_value > 21 and has_ace:
        total_card_value = total_card_value-10
    # Return the final value
    return total_card_value


# Draws card from the assembled deck (always the topmost one)
def drawCard(deck_name, player_name):
    current_card = deck_name[0]
    # Appends the chosen card to the players hand and deletes it from the deck
    playerCards[player_name].append(current_card)
    deck_name.pop(0)
    return deck_name, playerCards


with open("leaderboard.csv", 'r') as f:
    header = next(f)

    leaderData = []
    for row in f:
        leaderData.append(row.strip('\n'))

with open('rules.txt') as f:
    rules = f.readlines()

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

startChips = 100    # coins
playerCoins = {}
playerBets = {}
lost = []

stats = []
maxStats = 10
fields_name = ['Username', 'Coins']
entriesNo = 5

# Min and max of players that can play in one game
minPlayers = 1
maxPlayers = 7

minDecks = 2
maxDecks = 8

# Dealers display name
dealer = 'The Dealer'

decksAmount = 0

playerNames = []
playerCards = {}

# Template for assembling the actual deck
deckTemplate = [{'value': value, 'sign': sign} for value in values for sign in signs]
# The deck
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
        # Ask for players desired location
        menuOption = input('Your option: ')
  
        # Checks input validity and assigns correct bool vals to the variables
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
        splitData = []
        print()
        print('Here is the leaderboard!')
        print('Top ', entriesNo, ': ')
        print('Username - coins')
        for data in leaderData:
            splitData.append(data.split(','))

        for data in splitData:
            data[1] = int(data[1])

        splitData.sort(key=lambda x: x[1], reverse=True)
        for entries in range(1, entriesNo+1):
            print(entries-1, ') ', splitData[entries-1][0], ' - ', splitData[entries-1][1])

        atMenu, atLeaderBoard = goBack(atMenu, atLeaderBoard)

    while inGame:
        invalidDecksAmount = True
        deletePlayers = False
        inRound = True
        
        # If there are usernames already created, choose to leave or delete them
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
            # Check if there aren't already created decks
            if decksAmount != 0:

                # Can choose to play with the same number of decks or new one
                newAmount = input('Play with different amount of decks? [Y/N]: ')
                print('Current amount is: ', decksAmount)
                if newAmount.lower() == 'y':
                    decksAmount = input('How many decks do you want to use? [1-8]: ')

                    # If the decksAmount is a number and withing the 1-8 boundaries, set the new value
                    if decksAmount.isnumeric():
                        if 1 <= int(decksAmount) <= 8:
                            print('The game will be played with ', decksAmount, ' deck(s)')
                            invalidDecksAmount = False
                        else:   # Selected deck amount is invalid
                            print('Invalid amount of decks')
                            decksAmount = 0
                    else:   # The decksAmount is not a number
                        decksAmount = 0
                elif newAmount.lower() == 'n':
                    print('The game will be played with ', decksAmount, ' deck(s)')
                    invalidDecksAmount = False
            else:   # Deck amount wasn't selected yet
                decksAmount = input(f'How many decks do you want to use? [{minDecks}-{maxDecks}]: ')
                if decksAmount.isnumeric():
                    if minDecks <= int(decksAmount) <= maxDecks:
                        print('The game will be played with ', decksAmount, ' deck(s)')
                        invalidDecksAmount = False
                    else:   # Does not reflect 1-8
                        print('Invalid amount of decks')
                        decksAmount = 0
                else:   # decksAmount is not a number
                    decksAmount = 0

        # print(len(deck))
        inAddPlayer = True

        # While in player creation
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
                    if playerNames.count(player) != 0 or player.lower() == dealer.lower():
                        invalidInput = False
                    else:
                        playerNames.append(player)

                        print('Player has been added')
                        print('Current number of players is: ', len(playerNames))
                        if len(playerNames) >= 7:
                            invalidInput = False
                            addplayer = False
                            inAddPlayer = False
                            print('You reached max number of players!')
                            wait = input('continue [press enter]')
                        while invalidInput:
                            invalidInput = False
                            anotherPlayer = input('Do you want to add another player? [Y/N]: ')
                            if anotherPlayer.lower() == 'y':
                                addplayer = True
                            elif anotherPlayer.lower() == 'n':
                                addplayer = False
                                inAddPlayer = False
                            else:   # Not a valid input
                                invalidInput = True
        roundNo = 1
        while inRound:
            lost = []
            deck = []
            playerCards = {}
            stats = []
            # Keeps count of the while loop, must be less than amount of decks appended
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
                    playerCoins.update({player: 100})

            for i in range(2):
                deck, playerCards = drawCard(deck, dealer)
                for player in playerNames:
                    deck, playerCards = drawCard(deck, player)
            print('**********************')
            print('Upcard is: ', playerCards[dealer][0]['value'], ' - ', playerCards[dealer][0]['sign'])
            print('**********************')
            # print(playerNames)
            # print(playerChips)
            # print(playerCards)
            print('Place your bets!')
            for player in playerNames:
                print('-------------------------------')
                print('Player: ', player)
                print('You have: ', playerCoins[player], ' coins')
                invalidInput = True
                while invalidInput:
                    bet = input('Your bet: ')
                    if bet.isnumeric():
                        if 0 < int(bet) <= playerCoins[player]:
                            playerBets.update({player: int(bet)})
                            playerCoins[player] = playerCoins[player] - int(bet)
                            invalidInput = False
            print(playerCoins)
            for player in playerNames:
                wrongInput = True
                wait = input('continue [press enter]')
                print('-------------------------------')
                print('PLAYER: ', player)
                print('Your cards are: ')
                for card in playerCards[player]:
                    print(card['value'], ' - ', card['sign'], end=', ')
                print()
                print('Total: ', totalValue(cardsValues, playerCards, player))
                doubleDown = 'n'
                if totalValue(cardsValues, playerCards, player) == 21:
                    print('Blackjack! Wait for the results')
                    wrongInput = False
                # print('Turn of: ', player)
                elif playerCoins[player] >= playerBets[player]:
                    invalidInput = True
                    print('You can use double down!')
                    print('If you choose [Y] you will double the bet, draw one card and the round ends for you.')
                    print('Your current bet is: ', playerBets[player])
                    while invalidInput:
                        doubleDown = input('Double down? [Y/N]: ')
                        invalidInput = False
                        if doubleDown.lower() == 'y':
                            deck, playerCards = drawCard(deck, player)
                            playerCoins[player] = playerCoins[player] - playerBets[player]
                            playerBets[player] = playerBets[player] * 2
                            print(playerBets[player])
                            print('Your current bet is: ', playerBets[player], ' coins')
                            print('You drew: ', playerCards[player][-1]['value'], ' - ', playerCards[player][-1]['sign'])
                            print('Your new total is: ', totalValue(cardsValues, playerCards, player))
                        # player failed to input [y] or [n]
                        elif doubleDown.lower() != 'n':
                            invalidInput = True
                if doubleDown.lower() == 'n':
                    while wrongInput:
                        wrongInput = False
                        choice = input('Do you choose to Stand or Hit? [S/H]: ')
                        if choice.lower() == 's':
                            print('You chose to stand.')
                        elif choice.lower() == 'h':
                            print('You chose to hit')
                            wrongInput = True
                            deck, playerCards = drawCard(deck, player)
                            print('You drew: ', playerCards[player][-1]['value'], ' - ',
                                  playerCards[player][-1]['sign'])
                            print('New total: ', totalValue(cardsValues, playerCards, player))
                            if totalValue(cardsValues, playerCards, player) > 21:
                                coins = playerBets[player]
                                print('You went bust and lost: ', coins, ' coins')
                                wrongInput = False
                            elif totalValue(cardsValues, playerCards, player) == 21:
                                print('21! Wait for the game results.')
                                wrongInput = False
                        else:
                            wrongInput = True
            wait = input('continue [press enter]')
            # TODO: change the leaderboard, write data from for loop, one by one
            print('-------------------')
            print(dealer, ': ')
            dealer_total = totalValue(cardsValues, playerCards, dealer)
            print('Total: ', dealer_total)
            for cards in playerCards[dealer]:
                print(cards['value'], ' - ', cards['sign'], end=', ')
            print()
            while dealer_total < 17:
                deck, playerCards = drawCard(deck, dealer)
                dealer_total = totalValue(cardsValues, playerCards, dealer)
                # print(playerCards[dealer])
            print('New Total: ', dealer_total)
            print('Cards: ')
            for cards in playerCards[dealer]:
                print(cards['value'], ' - ', cards['sign'], end=', ')
            print()
            wait = input('continue [press enter]')

            # New attempt at showing dealers cards
            dealer_total = totalValue(cardsValues, playerCards, dealer)
            print()
            if dealer_total > 21:
                print('The dealer went bust! ')
                print('Their total is: ', dealer_total)
            elif dealer_total == 21:
                if len(playerCards[dealer]) == 2:
                    print('The dealer has blackjack!')
                else:   # Dealers total is 21 but they have >2 cards
                    print('The dealer won!')
                    print('Their total is 21')
            else:  # Dealers total is less then 21
                print('The dealer has total lower then 21 (', dealer_total, ')')
            wait = input('continue [press enter]')

            # evaluation of players points
            for player in playerNames:
                coins = 0
                bet = playerBets[player]
                total = totalValue(cardsValues, playerCards, player)
                if total == 21:
                    if dealer_total == 21:
                        coins = bet
                        # the bet is returned to the player
                    else:   # Dealers total differs from 21
                        coins = ((playerBets[player] + ((3 / 2) * bet)) // 1)
                        print(coins)
                elif total < 21:   # players total is under 21
                    # players total is more then dealers, wins double the bet
                    if dealer_total < total or dealer_total > 21:
                        coins = bet * 2
                    # equal totals, bet is returned
                    elif dealer_total == total:
                        coins = bet
                playerCoins[player] = playerCoins[player] + coins

            for player in playerNames:
                print('-------------------')
                print('Player: ', player)
                print('Total: ', totalValue(cardsValues, playerCards, player))
                print('Coins left: ', playerCoins[player])
                if playerCoins[player] == 0:
                    lost.append(player)
                print(playerNames)
                wait = input('continue [press enter]')

            # every player that hit 0 coins will be removed from all lists
            for player in lost:
                playerBets.pop(player)
                playerCoins.pop(player)
                playerNames.remove(player)

            if len(playerNames) != 0:
                for player in playerNames:
                    stats.append({'Username': player, 'Coins': playerCoins[player]})

                # appends stats with username and coins into a csv file
                with open('leaderboard.csv', 'a', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fields_name)

                    # writes one entry per line (username, coinsNo) from list
                    for row in stats:
                        writer.writerow(row)
            else:   # there are no players left, all hit 0 coins, gets them to the menu
                print('Everyone lost all of their coins.')
                print('You will now be transported to the menu!')
                wait = input('continue [press enter]')

            # at the end use can choose to go back to the main menu or play another round
            playAgain = True

            # if all the players get to 0 coins, get back to menu
            if len(playerNames) == 0:
                inRound = False
                inGame = False
                atMenu = True
                playAgain = False

            # until the player chooses a valid option, repeat
            while playAgain:
                again = input('Play another round? [Y/N]: ')
                # will start another round
                if again.lower() == 'y':
                    # for keeping track of how many rounds have been played
                    # first round everyone gets starter 100 coins
                    roundNo = roundNo + 1
                    inRound = True
                    playAgain = False
                # transports the player(s) to the menu
                elif again.lower() == 'n':
                    inRound = False
                    playAgain = False
                    atMenu, inGame = goBack(atMenu, inGame)

    # writes out rules from a txt file for the player(s) to see
    while atRules:
        print()
        print()
        # writes out rules one by one
        for rule in rules:
            print(rule, end='')
        atMenu, atRules = goBack(atMenu, atRules)
