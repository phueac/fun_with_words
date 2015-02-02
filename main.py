import json
import random

def random_word(words, first_char):
    """Returns a random word from words which starts with the letter
    first_char."""
    possibilities = [w for w in words.keys() if w.startswith(first_char.upper())]
    choice = random.randint(0, len(possibilities) - 1) 
    return possibilities[choice].lower()

if __name__ == '__main__':
    # Read words from dictionary
    fin = open('dictionary/dictionary.json', 'r')
    words = json.load(fin)
    fin.close()

    print random_word(words, 'e')
