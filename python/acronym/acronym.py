import re


def abbreviate(words):
    list_of_words = re.sub("[^A-Za-z']+", ' ', words).split(" ")
    return "".join([word[0].upper() for word in list_of_words])
