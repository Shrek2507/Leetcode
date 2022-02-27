import random
import re
import nltk
from nltk.corpus import words


# func to make a guess...
def make_guess(valid_words):
    return random.choice(valid_words).upper()


# func to collect the result...
def collect_result():
    # Collect the result of our guess from the user...
    result = input().upper()
    match = re.match(r'[A-Z]{5}$', result)
    if not match:
        print("Invalid response string, try again")
        return collect_result()

    return result


# func to get a result...
def get_result(guess, answer):
    # Given a guess and a known answer, return the result
    result = ""
    for pos, ch_guess, ch_answer in zip(range(5), guess, answer):
        if ch_guess == ch_answer:
            result += "1"
        elif ch_answer in guess:
            result += "2"
        else:
            result += "3"
    return result


def update_valid_words(valid_words, guess, result):
    return [word for word in valid_words if get_result(guess, word) == result]


if __name__ == "__main__":
    word_list = words.words()
    # get a list of valid words...
    valid_words = [word.upper() for word in word_list if len(word) == 5]

    # Storing the Random guessed word...
    #guess = make_guess(valid_words)
    guess = "SPEED"

    totalAttempts = 6
    for attempt in range(1, totalAttempts+1):
        # Collect the users word...
        user_word = collect_result()
        result = get_result(guess, user_word)
        print("FEEDBACK : ", result)
        if result == '11111':
            print(
                f'Congratulations The Wordle is solved in {attempt} attempts')
            break
        elif result != '11111' and attempt != 6:
            continue
        else:
            print(f'SORRY the wordle is not solved. The correct word was : ', guess)
            break
