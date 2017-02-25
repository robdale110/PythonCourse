import string, random
r"""

    This script takes input and generates names from the
    input.

"""
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
all_letters = string.ascii_lowercase
first_letter_input = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, l for any letters: ")
second_letter_input = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, l for any letters: ")
third_letter_input = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, l for any letters: ")

def generator():
    if (first_letter_input == "v"):
        first_letter = random.choice(vowels)
    elif (first_letter_input == "c"):
        first_letter = random.choice(consonants)
    elif (first_letter_input == "l"):
        first_letter = random.choice(all_letters)
    else:
        first_letter = first_letter_input

    if (second_letter_input == "v"):
        second_letter = random.choice(vowels)
    elif (second_letter_input == "c"):
        second_letter = random.choice(consonants)
    elif (second_letter_input == "l"):
        second_letter = random.choice(all_letters)
    else:
        second_letter = second_letter_input

    if (third_letter_input == "v"):
        third_letter = random.choice(vowels)
    elif (third_letter_input == "c"):
        third_letter = random.choice(consonants)
    elif (third_letter_input == "l"):
        third_letter = random.choice(all_letters)
    else:
        third_letter = third_letter_input

    name = first_letter + second_letter + third_letter
    return name

for i in range(20):
    print(generator())
