import random
# leaderboard, write into a new file
# at the start is a menu (startgame, leaderboard)
# save cards into a dictionary
# shuffle is a function in python to shuffle the dictionary
# always take the 0. card
# do not use random choice, but radnom shuffle instead (the dictionary)


# Function to get back to the main menu
def goBack(at_menu, at_place):
    wrongInput = True
    while wrongInput:
        go_back = input('Return back: [press enter]')
        if go_back == '':
            at_menu = True
            at_place = False
            wrongInput = False
    return at_menu, at_place


def hit_stand():
    choice = input('Do you want to stand or hit? [S/H]')


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
signs = ['H', 'D', 'C', 'S']

chipsVal = [1, 5, 25, 100, 500, 1000]

minPlayers = 1
maxPlayers = 7

deck = [{'value': value, 'sign': sign} for value in values for sign in signs]

programRunning = True
atMenu = True
inGame = False
atLeaderBoard = False

print('Blackjack')
print()

while programRunning:
    print()
    print('Start the game [0]')
    print('See the leaderboard [1]')

    while atMenu:
        menuOption = input('Your option: ')

        if menuOption.isnumeric():
            if int(menuOption) == 0:
                print('The game is starting...')
                atMenu = False
                inGame = True
            elif int(menuOption) == 1:
                print('Loading the leaderboard')
                atMenu = False
                atLeaderBoard = True
            else:   # invalid number value
                atMenu = True
        else:   # option is not a number
            atMenu = True

    while atLeaderBoard:
        print('Here is the leaderboard!')

        # at the end use can choose to go back to the main menu
        atMenu, atLeaderBoard = goBack(atMenu, atLeaderBoard)

    while inGame:
        print('Start')

        # at the end use can choose to go back to the main menu
        atMenu, inGame = goBack(atMenu, inGame)
