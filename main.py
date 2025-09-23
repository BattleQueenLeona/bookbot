def get_book_text(path):
    with open (path) as f:
        file_contents = f.read()
    return file_contents

def main():
    from stats import count_words
    from stats import count_letters,  sort_letter_counts
    import sys
    path = 0
    try:
        path = sys.argv[1]
    except Exception:
            print ("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
    words = get_book_text(path)
    wordcount = count_words(words)
    count_of_characters = count_letters(words)
    list_of_letter_counts = sort_letter_counts(count_of_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    #displaying all letter counts in order:
    for letter in list_of_letter_counts:
        count = letter["count"]
        alpha = letter["letter"]
        print(f"{alpha}: {count}")



main()