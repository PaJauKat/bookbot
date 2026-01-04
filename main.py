from stats import get_num_words, calculate_characters, sort_characters_by_frequency
import sys

def get_book_text(path):
    with open(path) as file:
        return file.read()
    

    
def main():
    print("============ BOOKBOT ============")

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)

    print("----------- Word Count ----------")
    get_num_words(book_text)

    print("--------- Character Count -------")
    characters = calculate_characters(book_text)
    sorted_chars = sort_characters_by_frequency(characters)
    [print(f"{c}: {n}") for c,n in sorted_chars]
    print("============= END ===============")

main()