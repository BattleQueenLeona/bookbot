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

def sort_on(items):
    return items["count"]

def sort_letter_counts (letter_count):
    count_list = []
    for character in letter_count:
        if character.isalpha():
            count_list.append({"letter": character,"count" : letter_count[character]})
    count_list.sort(reverse=True, key=sort_on)
    return count_list
