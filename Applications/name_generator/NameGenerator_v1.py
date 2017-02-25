import string, random
r"""

    This script takes input and generates names from the
    input.

"""
def generator():
    first_letter = random.choice(string.ascii_lowercase)
    second_letter = random.choice(string.ascii_lowercase)
    third_letter = random.choice(string.ascii_lowercase)

    name = first_letter + second_letter + third_letter

    return name

print(generator())
