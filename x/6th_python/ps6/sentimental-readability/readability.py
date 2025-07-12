# TODO
from cs50 import get_string


def main():
    text = get_string("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)
    if index < 1:
        print("Before Grade 1")
    elif index > 15:
        print("Grade 16+")
    else:
        print("Grade", index)


def count_letters(text):
    i = 0
    for c in text:
        if c.isalpha():
            i += 1
    return i


def count_words(text):
    return len(text.split())


def count_sentences(text):
    return text.count(".") + text.count("!") + text.count("?")


main()
