def distance(strand_a, strand_b):
	if len(strand_a) != len(strand_b):
		raise ValueError("Improper Arguments")
	return len([b for a, b in zip(strand_a, strand_b) if a != b])