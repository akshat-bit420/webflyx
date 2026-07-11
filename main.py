import sys

from stats import text_to_words, count_all_words, chars_dict_to_sorted_list


def get_book_text(path) -> str:
    with open(path) as f:
        return f.read()


def print_report(book_path, total_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for character, count in sorted_chars:
        if not character.isalpha():
            continue
        print(f"{character}: {count}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    read_content = get_book_text(book_path)

    total_words = text_to_words(read_content)

    counted_words = count_all_words(read_content)

    sorted_chars = chars_dict_to_sorted_list(counted_words)

    print_report(book_path, total_words, sorted_chars)


if __name__ == "__main__":
    main()
