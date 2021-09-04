"""
file: seven_sgmt_longest_word
description: find the longest english word that can be made using a seven segment display
language: python3
author: Hritik "Ricky" Gupta
"""

BAD_LETTERS = ['g', 'i', 'k', 'm', 'q', 'v', 'w', 'x', 'z']

def find_longest_word(filename):
    """
    find the longest word not including the characters specified in BAD_LETTERS
    :param filename: a filename
    :return: list containing all longest acceptable words
    """
    f = open(filename)
    longest_acceptable_word = ''
    longest_acceptable_words = []
    for line in f:
        line = line.strip()
        if len(line) < len(longest_acceptable_word):
            continue
        letters = list(line)
        if test_bad_letters(letters):
            continue
        if longest_acceptable_words and len(line) > len(longest_acceptable_words[0]):
            longest_acceptable_words.clear()
        longest_acceptable_word = line
        longest_acceptable_words.append(longest_acceptable_word)
    f.close()
    return longest_acceptable_words

def test_bad_letters(letters):
    """
    tests letters of a given word to see if they are in BAD_LETTERS
    :param letters: a list of letters
    :return: True if letter is found to be in BAD_LETTERS, False otherwise
    """
    for letter in BAD_LETTERS:
        if letter in letters:
            return True
    return False

def main():
    file = input("What is the name of the file? ")
    words = find_longest_word(file)
    print("Here are the longest acceptable words: ")
    print(words)

if __name__ == '__main__':
    main()