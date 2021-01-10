def is_pangram(sentence):
	return all(alphabet in sentence.lower() for alphabet in "abcdefghijklmnopqrstuvwxyz")
