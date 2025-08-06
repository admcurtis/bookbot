
#%% DEPENDENCIES
from collections import defaultdict

#%% FUNCTIONS
def get_num_words(text):
    split_string = text.split()
    num_words = len(split_string)
    return num_words


def get_num_chars(string_to_count):

    char_dict = defaultdict(int)

    alpha_only = [char.lower() for char in string_to_count if char.isalpha()]

    for character in alpha_only:
        char_dict[character] += 1

    return char_dict


def sort_dict(num_chars):

    x = [{"name": c, "num": n} for c, n in num_chars.items()]

    x.sort(reverse=True, key=lambda item: item["num"])

    return x 