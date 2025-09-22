def count_words(text):
    import string
    wordcount = 0 
    text_words = text.split()
    wordcount = len(text_words)
    return wordcount

def count_letters(text):
    letter_count = {}
    text = text.lower()
    for character in text:
        if character not in letter_count:
            letter_count[character] = 1
        else:
            letter_count[character] += 1
    return letter_count

#def sort_letter_counts (letter_count):
#    return letter_count["count"]
