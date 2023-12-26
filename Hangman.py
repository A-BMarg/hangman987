import string

word_list = ['apple', 'banana', 'mango', 'grapes', 'pineapple']
#print(word_list)
import random
word = random.choice(word_list)
print(word)
guess = input('input a single letter: ')

if len(guess) == 1 and guess in string.ascii_lowercase:
  print("Good guess!")
else:
  print("Oops! That is not a valid input.")