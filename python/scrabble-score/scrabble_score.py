score_table = {}

for char in "AEIOULNRST":
	score_table[char] = 1
for char in "DG":
	score_table[char] = 2
for char in "BCMP":
	score_table[char] = 3
for char in "FHVWY":
	score_table[char] = 4
for char in "K":
	score_table[char] = 5
for char in "JX":
	score_table[char] = 8
for char in "QZ":
	score_table[char] = 10

def score(word):
	return sum([score_table[letter.upper()] for letter in word])