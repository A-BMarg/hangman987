#The check_guess function will take the guessed letter as an argument and check if the letter is in the word.
#The ask_for_input function will check if the input is a valid guess

word = 'apple'
guess = input('input a single letter: ')

def check_guess(guessed_letter):
  if guess.lower() in word:
    print(f'Good guess! {guess} is in the word.')
  else:
    print(f'Sorry, {guess} is not in the word. Try again.')

def ask_for_input():
  while True:

    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
    break
  
  check_guess(guess)

ask_for_input()