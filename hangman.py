import random

# saves words from 2 files into 2 lists (1 line = 1 value) by difficulty
with open("words.txt") as f:
    words = f.read().splitlines()
with open("difficultWords.txt") as f:
    difficultWords = f.read().splitlines()


# Function that takes letter, that the player guesses,
# word, that is being guessed and the word with hidden letters
def guess_letter(letter, word, hidden):
    is_correct: bool = False
    # searches for the guessed letter in the word
    if letter in word:
        is_correct: bool = True
        # serches for index of the letter, if it was found
        for p in range(0, len(word)):
            if word[p] == letter:
                # changes the values of the positions of the found letter from '_' to letter
                hidden = hidden[0:p] + letter + hidden[p + 1:len(word)]
    # returns 2 variables, whether the letter was found (is_correct) and the updated hidden word
    return is_correct, hidden


winRate = 0
lost = 0
win = 0

contn: bool = True
print("The Hangman")
print()
while contn:
    # declaring the number of lives the player will work with in the game
    lives = 8
    guess_word = ""
    contn2 = True
    while contn2:
        # Player chooses the difficulty, random index number is chosen and found in the coresponidng list
        difficulty = input('Difficulty level - normal(1), nightmare(2): ')
        contn2 = False
        if difficulty == '1':
            random_no: int = random.randint(0, len(words) - 1)
            guess_word = words[random_no]
        elif difficulty == '2':
            random_no: int = random.randint(0, len(difficultWords) - 1)
            guess_word = difficultWords[random_no]
        else:
            print('Ivalid input!')
            contn2 = True

    print()
    print()
    print('Guess the word:')

    # Change all chars to '_'
    hidden_word = '_' * len(guess_word)
    print(len(guess_word), 'letters')
    for i in hidden_word:
        print(i, end=" ")

    # Defining lists to store letters in
    letters = []
    wrong_letters = []

    while lives > 0:
        letterA = ''
        contn3 = True
        while contn3:
            # Checking whether the player input is only 1 letter
            print()
            letterA = input('Guess letter: ').lower()
            if len(letterA) == 1 and letterA.isalpha():
                if letterA in letters:
                    contn3 = True
                else:
                    contn3 = False
            else:
                contn3 = True

        # Saving returned info into 2 variables, found (whether the letter exists in the word)
        # and hidden_word (letters with '_')
        found, hidden_word = guess_letter(letterA, guess_word, hidden_word)

        # If the letter was already guessed it's not going save in the list
        if letterA in letters:
            again = True
        else:
            again = False
            letters.append(letterA)
            if letterA not in hidden_word:
                wrong_letters.append(letterA)

        # Printing out all the current info about the game state to the player
        for i in hidden_word:
            print(i, end=" ")
        print()
        print('Letters: ', end="")

        for i in letters:
            print(i, end=" ")
        print()

        print('Wrong letters: ', end="")

        for i in wrong_letters:
            print(i, end=" ")
        print()

        if not found and not again:
            lives -= 1
            if lives == 0:
                print('Game lost, word you were guessing was: ', guess_word)

                lost += 1
                contn4 = True

                # Player decides whether they want to continue playing or not
                while contn4:
                    play = input('Play again? [Y,N]: ')
                    if play.lower() == 'y':
                        contn = True
                        contn4 = False
                    elif play.lower() == 'n':
                        contn = False
                        contn4 = False
                    else:
                        contn4 = True

                # Printing out the games stats
                if lost > 0 or win > 0:
                    print()
                    print('Results so far: ')

                    print('You won: ', win, ' time(s)')
                    print('And you lost: ', lost, ' time(s)')

                    if lost != 0:
                        winRate = round((win / (win+lost))*100)

                    print('Your winrate is: ', winRate, ' %')

                break
            elif not found:
                print('The letter was not found, remaining lives: ', lives)
                for i in hidden_word:
                    print(i, end=" ")
                print()
            else:
                pass
        else:
            if "_" not in hidden_word:
                print('You correctly guessed the word! Remaining lives: ', lives)
                print('The word is: ', guess_word)

                win += 1
                contn5 = True
                while contn5:
                    play = input('Play again? [Y,N]: ')
                    if play.lower() == 'y':
                        contn = True
                        contn5 = False
                    elif play.lower() == 'n':
                        contn = False
                        contn5 = False
                    else:
                        contn5 = True

                if lost > 0 or win > 0:
                    print()
                    print('Results so far: ')

                    print('You won: ', win, ' time(s)')
                    print('And you lost: ', lost, ' time(s)')

                    if lost != 0:
                        winRate = round((win / (win+lost))*100)

                    print('Your winrate is: ', winRate, ' %')

                break
            else:
                print('The letter was found, lives remaining: ', lives)
                for i in hidden_word:
                    print(i, end=" ")
                print()
