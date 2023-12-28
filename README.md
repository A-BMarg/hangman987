# Hangman

Description:
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game that asks the user for a letter and checks if it is in the word.
It starts with a default number of lives and a random word from the word_list.

File structure of the project:   
Class: Hangman

  Parameters:
      
      word_list: list
          List of words to be used in the game
      num_lives: int
          Number of lives the player has, set at default 5
      
  Attributes:
  
      word: str
          The word to be guessed picked randomly from the word_list
      word_guessed: list
          A list of the letters of the word, with '_' for each letter not yet guessed
          For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
          If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
      num_letters: int
          The number of UNIQUE letters in the word that have not been guessed yet
      num_lives: int
          The number of lives the player has
      list_of_guesses: list
          A list of the letters that have already been tried

  Methods:
  
    check_guess(guess)
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.
      Parameters:
        guess: str
            The letter to be checked   
    
    ask_for_input()
        Asks the user for a guess in the form of a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single alphanumeric character
        If it passes both checks, it calls the check_guess method.

  Function:
  
    play_game(word_list)
      Function that runs the Hangman game as expected.
    
    Parameters:
        word_list: list
            List of words to be used in the game   

    Within function:
  
    1. Creates an instance of the Hangman class.
  
     Parameters:
        word_list: list
            List of words to be used in the game  
        num_lives: int
            Number of lives the player has, set at default 5
          
    Checks if the num_lives is 0. 
    If it is, the game ends and the user loses.
    Checks if the num_letters is greater than 0. 
    If it is, the ask_for_input method is called.
    If above not satisfied, that means the user has won the game. 
  
Installation instructions

Usage instructions

License information
