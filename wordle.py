import random
import sys
from termcolor import colored
import nltk
from nltk.corpus import words


# func to print menu
def print_menu():
    print("Lets play Wordle...")
    print('Type a 5 letter word and hit enter : \n')


# function to read random word...
def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)


nltk.data.path.append('/work/words')
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]

print_menu()
word = random.choice(words_five)
totalGuessCount = 6
# print(word)

for attempt in range(1, totalGuessCount+1):
    guess = input().lower()

    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

    # Validate if the length of the guessed word is 5...
    for i in range(min(5, len(guess))):
        if guess[i] == word[i]:
            print(colored(guess[i], 'green'), end="")

        elif guess[i] in word:
            print(colored(guess[i], 'yellow'), end="")

        else:
            print(colored(guess[i]), end="")

    if guess == word:
        print(colored(f'Congrats!!! YOU WON IN {attempt} attempts', "red"))
        break

    elif attempt == 6:
        print(colored(f'SORRY The Actual word was {word}'))
