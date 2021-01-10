def is_armstrong_number(number):
	digits = list(map(int, str(number)))
	number_of_digits = len(digits)
	sum = 0
	for digit in digits:
		sum += digit**number_of_digits
	return True if sum == number else False