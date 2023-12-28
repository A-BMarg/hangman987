import random
import string

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list) #The word to be guessed, picked randomly from the word_list
        self.word_guessed = ['_'] * len(self.word)
        #A list of the letters of the word, with _ for each letter not yet guessed.
        #For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_'].
        #If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        self.num_letters = int(len(set(self.word))) #The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives #The number of lives the player has at the start of the game.
        self.word_list = word_list #A list of words
        self.list_of_guesses = [] #A list of the guesses that have already been tried. Set this to an empty list initially


    def ask_for_input(self):
        while True:
            guess = input('input a single letter: ')
            if len(guess) != 1:
              print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess not in string.ascii_lowercase:
              print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
              print("You already tried that letter!")
            else:
              self.check_guess(guess)
              self.list_of_guesses.append(guess)
              break

    def check_guess(self, guess):
      guess = guess.lower()
      if guess in self.word:
          print(f'Good guess! {guess} is in the word.')
          self.word_guessed = ['_'] * len(self.word)
          #print(word_guessed)
          for x in range(len(self.word)):
            if self.word[x] == guess:
              self.word_guessed[x] = guess
              print(self.word_guessed)
          self.num_letters -= 1

      else:
          print(f'Sorry, {guess} is not in the word. Try again.')
          self.num_lives -=1
          print(f'You have {self.num_lives} lives left.')


def play_game(word_list):
        num_lives = 5

        game = Hangman(word_list, num_lives)

        while True:
          if game.num_lives == 0:
            print("You lost!")
            break

          if game.num_letters >0:
            game.ask_for_input()
          else: #num_lives != 0 and num_letters !> 0:
            print('Congratulations. You won the game!')
            break

word_list = ['hippoptamus', 'moose', 'gorilla', 'skyscraper', 'moon', 'sandals', 'cream', 'monster', 'australia', 'mission', 'atlanta', 'president']
play_game(word_list)


