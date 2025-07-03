from stats import word_count
from stats import count_characters
from stats import sort_char_count
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open (file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    content = get_book_text(sys.argv[1])

    num_words = word_count(content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    num_char = count_characters(content)
    sort_count = sort_char_count(num_char)

    for item in sort_count:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
