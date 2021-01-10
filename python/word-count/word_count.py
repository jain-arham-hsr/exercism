import re
from collections import *

def count_words(sentence):
	words = re.sub("[^A-Za-z0-9']+", ' ', sentence).split(" ")
	words = list(filter(None, words))
	count = Counter()
	for word in words:
		count[word.rstrip("'").lstrip("'").lower()] += 1
	return count