import itertools

def is_palindrome(num):
    num = str(num)
    return num == num[::-1]

def validate_input(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Minimum factor cannot be greater than maximum factor.")

def largest(min_factor, max_factor):
    validate_input(min_factor, max_factor)
    combinations = itertools.combinations(range(min_factor, max_factor + 1), 2)
    possible_products = list(map(lambda combination: combination[0] * combination[1], combinations))
    res_value = max(filter(is_palindrome, set(possible_products)), default=None)
    res_factors = [combinations[index] for index, product in enumerate(possible_products) if product == res_value]
    return res_value, res_factors

def smallest(min_factor, max_factor):
    validate_input(min_factor, max_factor)
    combinations = list(itertools.combinations(range(min_factor, max_factor + 1), 2))
    possible_products = list(map(lambda combination: combination[0] * combination[1], combinations))
    res_value = min(filter(is_palindrome, set(possible_products)), default=None)
    res_factors = [combinations[index] for index, product in enumerate(possible_products) if product == res_value]
    return res_value, res_factors
