def classify(number):
    if number <= 0:
        raise ValueError("Invalid Input. Only Natural Numbers accepted.")
    factors = sum([[n, number/n] for n in range(1, int(number**0.5)+1) if number % n == 0], [])
    factors.remove(number)
    factors = list(set(factors))
    aliquot_sum = sum(factors)
    if aliquot_sum == number and aliquot_sum != 1:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
