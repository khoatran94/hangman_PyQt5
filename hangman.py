import string
import random


def pick_word():
    with open('words_alpha.txt', 'r') as f:
        wordlist = f.read().strip('\n').split('\n')
    word = random.choice(wordlist)
    return word.upper()

def hangman():

    #inintaialize the game
    lives = 6
    word = pick_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed_words = []

    while len(word_letters)>0 and lives>0:

        #keeping track of player's guesses
        print('Live(s) left : {}'.format(lives))
        print("Used letter: {}".format(''.join(guessed_words)))
        indicator = [letter if letter in guessed_words else '-' for letter in word]
        print('Current word: {}\n'.format(' '.join(indicator)))

        #player input
        letter = input('Guess a word: ').upper()
        print('\n')

        #checking player next guess
        if letter in alphabet-set(guessed_words):
            guessed_words.append(letter)
            if letter in word_letters:
                word_letters.remove(letter)
            else:
                print('{} is not in the word'.format(letter.upper()))
                lives-=1
        elif letter in guessed_words:
            print('Letter is already guessed.')
        else:
            print('Word contains only alphbetical letters.')

    if lives == 0:
            print('Congratulations!!!')
            print('The word is {}'.format(word.upper()))
    else:
            print('Better luck next time')
            print('The word is {}'.format(word.upper()))






hangman()