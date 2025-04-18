import sys
from stats import count_words, count_letters, sort_character_counts


def main():
    # Check if we have the right number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the path from command-line arguments
    path = sys.argv[1]
    
    # Read the contents of the book
    with open(path) as f:
        contents = f.read()
    
    # The rest of your function remains the same
    word_count = count_words(contents)
    char_frequency = count_letters(contents)
    sorted_chars = sort_character_counts(char_frequency)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    # The rest of your print statements...
    
    # Print each character count (alphabetic characters only)
    for char_dict in sorted_chars:
        char = char_dict["character"]
        count = char_dict["count"]
        # Only print alphabetic characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()