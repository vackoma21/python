import random

with open("words.txt") as f:
    words = f.read().splitlines()
with open("difficultWords.txt") as f:
    difficultWords = f.read().splitlines()


def guess_letter(letter, word, hidden):
    is_correct: bool = False
    if letter in word:
        is_correct: bool = True
        for p in range(0, len(word)):
            if word[p] == letter:
                hidden = hidden[0:p] + letter + hidden[p + 1:len(word)]

    return is_correct, hidden


contn: bool = True
print("The Hangman")
print()
while contn:
    lives = 10
    guess_word = ""
    contn2 = True
    while contn2:
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
    hidden_word = '_' * len(guess_word)
    print(len(guess_word))
    print(hidden_word)
    letters = []
    wrong_letters = []

    while lives > 0:
        letterA = ''
        contn3 = True
        while contn3:
            letterA = input('Guess letter: ')
            if len(letterA) == 1 and letterA.isalpha():
                if letterA in letters:
                    contn3 = True
                else:
                    contn3 = False
            else:
                contn3 = True

        found, hidden_word = guess_letter(letterA, guess_word, hidden_word)

        if letterA in letters:
            again = True
        else:
            again = False
            letters.append(letterA)
            if letterA not in hidden_word:
                wrong_letters.append(letterA)

        print(hidden_word)
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
                play = input('Play again? [Y,N]: ')

                if play.lower() == 'y':
                    contn = True
                else:
                    contn = False

                break
            elif found:
                print('The letter was not found, remaining lives: ', lives)
                print(hidden_word)
                print()
            else:
                pass
        else:
            if "_" not in hidden_word:
                print('You correctly guessed the word! Remaining lives: ', lives)
                play = input('Play again? [Y,N]: ')

                if play.lower() == 'y':
                    contn = True
                else:
                    contn = False

                break
            else:
                print('The letter was found, lives remaining: ', lives)
                print(hidden_word)
                print()
