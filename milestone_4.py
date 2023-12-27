import random
import string
list_of_guesses = []
word_list = ['hippoptamus', 'moose', 'gorilla', 'skyscraper', 'moon', 'sandals', 'cream', 'monster', 'australia', 'mission', 'atlanta', 'president']
word = random.choice(word_list)
print(word)


class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = word #The word to be guessed, picked randomly from the word_list
        self.word_guessed = word_guessed
        #A list of the letters of the word, with _ for each letter not yet guessed. 
        #For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. 
        #If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        self.num_letters = num_letters #The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives #The number of lives the player has at the start of the game.
        self.word_list = word_list #A list of words
        self.list_of_guesses = list_of_guesses #A list of the guesses that have already been tried. Set this to an empty list initially

    def ask_for_input(self):
        while True:
            guess = input('input a single letter: ')
            if len(guess) != 1:
              print("Invalid letter. Please, enter a single alphabetical character.") 
            elif guess not in string.ascii_lowercase:
              print("Invalid letter. Please, enter a single alphabetical character.")     
            elif guess in list_of_guesses:              
              print("You already tried that letter!")
            else:                           
              self.check_guess(guess)
    

                               
    def check_guess(self):
        if guess.lower() in word:
          print(f'Good guess! {guess} is in the word.')
          word_guessed = ['_'] * len(word)
          #print(word_guessed)
          for x in range(len(word)):
            if word[x] == guess:
              word_guessed[x] = guess
              print(word_guessed)

            w_list = list(word)
            print(w_list) 
            w_list[:] = (w for w in w_list if w != guess)
            print(w_list)
            num_letters = len(w_list)
            print(num_letters)       
            #num_letters -= 1
        
          else:
            print(f'Sorry, {guess} is not in the word. Try again.')  
            num_lives -= 1
            print(f'You have {num_lives} lives left.')
              
          list_of_guesses.append(guess)     

Hangman.ask_for_input()   
    