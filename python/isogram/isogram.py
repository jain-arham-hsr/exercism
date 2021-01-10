def is_isogram(string):
	letters = []
	for char in string.lower():
		if char.isalpha():
			if char in letters:
				return False
			else:
				letters.append(char)
	return True
