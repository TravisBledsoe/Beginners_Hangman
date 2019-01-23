# The user needs to be able to input letter guesses.
# A limit should also be set on how many guesses they can use.
# This means you’ll need a way to grab a word to use for guessing.
#  (This can be grabbed from a pre-made list. No need to get too fancy.)
#  You will also need functions to check if the user has actually inputted
#  a single letter, to check if the inputted letter is in the hidden word
#  (and if it is, how many times it appears), to print letters, and a counter
#  variable to limit guesses.
# Concepts to keep in mind:

# Random
# Variables
# Boolean
# Input and Output
# Integer
# Char
# String
# Length
# Print
# from random import choice

from random import choice

# Grab a word for guessing from a pre-made list
random_word_list = choice(["horse", "apple", "chair"])

# user input
input_char = input("What is your guess? ")

# User-defined function


def word_check():
    """
    1. Make sure guess is a single letter
    2. if that letter is in words_list
    3. how many times it appears in
    4. print the letters out
    5. counter to limit guesses
    """


letter_appears = 0  # 3
guess_limit = 5  # 5
while True:
    guess_limit += 1  # 5
    letter_appears += 1  # 1
    for letter in random_word_list:
        if letter in random_word_list:  # 2
            print(letter)  # 4
        else:
            print("Try again: ")  # 4
            break


# single_letter = 1  # 1
if len(input_char) > 1:
    print("Only 1 character allowed!")

word_check(input_char)
