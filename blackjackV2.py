import random
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


def hit_stand():
    choice = input('Do you want to stand or hit? [S/H]')
    invalid_choice = True

    while invalid_choice:
        if choice.lower() == 's':
            print('You chose to stand, next player:')
            invalid_choice = False
        elif choice.lower() == 'h':
            print('You chose to hit:')
            invalid_choice = False
        else:
            invalid_choice = True


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
signs = ['H', 'D', 'C', 'S']

chipsVal = [1, 5, 25, 100, 500, 1000]
startChips = 100    # dollars

minPlayers = 1
maxPlayers = 7

playerNames = []

deck = [{'value': value, 'sign': sign} for value in values for sign in signs]

programRunning = True
atMenu = True
inGame = False
atLeaderBoard = False
atRules = False

print('Blackjack')
print()

while programRunning:
    os.system('cls')
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
        os.system('cls')
        print('Here is the leaderboard!')

        # at the end use can choose to go back to the main menu
        atMenu, atLeaderBoard = goBack(atMenu, atLeaderBoard)

    while inGame:
        os.system('cls')
        invalidDecksAmount = True

        print('Start')

        while invalidDecksAmount:
            decksAmount = input('How many decks do you want to use? [1-8]: ')
            if decksAmount.isnumeric():
                if 1 <= int(decksAmount) <= 8:
                    print('The game will be played with ', decksAmount, ' deck(s)')
                    invalidDecksAmount = False
                else:
                    print('Invalid amount of decks')
        inAddPlayer = True

        while inAddPlayer:
            print('Create the player accounts.')

            addplayer = True
            while addplayer:
                player = input('Write your username, please: ')
                playerNames.append(player)

                print('Player has been added')
                print('Current number of players is: ', len(playerNames))
                anotherPlayer = input('Do you want to add another player? [Y/N]: ')
                if anotherPlayer.lower() == 'y':
                    addplayer = True
                elif anotherPlayer.lower() == 'n':
                    addplayer = False
                    inAddPlayer = False

        # at the end use can choose to go back to the main menu
        atMenu, inGame = goBack(atMenu, inGame)

    while atRules:
        os.system('cls')
        print('The Rules of The Game of Blackjack')
        print('Rule No.1: ')

        atMenu, atRules = goBack(atMenu, atRules)
