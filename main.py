#%% DEPENDENCIES
from stats import get_num_words, get_num_chars, sort_dict
import sys

#%%
def main():

    try:
        frank_string = get_book_text(sys.argv[1])
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    num_words = get_num_words(frank_string)
    num_chars = get_num_chars(frank_string)
    
    char_list = sort_dict(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for count in char_list:
        print(f"{count["name"]}: {count["num"]}")
    print("============= END ===============")


def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents


if __name__ == "__main__":
    main()    
    
