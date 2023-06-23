import string
import random

def pick_word():
    with open('words_alpha.txt', 'r') as f: #https://github.com/dwyl/english-words
        wordlist = f.read().strip('\n').split('\n')
    word = random.choice(wordlist)
    return word.upper()

class Hangman():
    def __init__(self):
        self.word = pick_word()
        self.guess_times = 0
        self.word_letters = set(self.word)
        self.alphabet = set(string.ascii_uppercase)
        self.guessed_words = []
        self.indicator = ' '.join([letter if letter in self.guessed_words else '-' for letter in self.word])

    def new_game(self):
        self.__init__()

    def guess(self, input_letter):
        input_letter = input_letter.upper()
        if input_letter in self.alphabet-set(self.guessed_words):
            self.guessed_words.append(input_letter)
            if input_letter in self.word_letters:
                self.word_letters.remove(input_letter)
            else:
                print('{} is not in the word'.format(input_letter.upper()))
                self.guess_times += 1
        elif input_letter in self.guessed_words:
            print('Letter is already guessed.')
        else:
            print('Word contains only alphbetical letters.')
        self.indicator = self.update_indicator()

    def update_indicator(self):
        self.indicator = ' '.join([letter if letter in self.guessed_words else '-' for letter in self.word])
        return self.indicator
