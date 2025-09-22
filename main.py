def get_book_text(path):
    with open (path) as f:
        file_contents = f.read()
    return file_contents

def main():
    from stats import count_words
    from stats import count_letters
    words = get_book_text("books/frankenstein.txt")
    wordcount = count_words(words)
    lettercount = count_letters(words)
    print (f"Found {wordcount} total words")
    print (f"And here's the mess of character counts!{lettercount}")



main()