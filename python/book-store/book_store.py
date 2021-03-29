from collections import Counter

PRICE_PER_BOOK = 8
DISCOUNT = {
    1: 0.00,
    2: 0.05,
    3: 0.10,
    4: 0.20,
    5: 0.25
}
PRICES = {i: (PRICE_PER_BOOK * (1 - DISCOUNT[i]) * i) for i in range(1, len(DISCOUNT) + 1)}

def total(basket):
    frequency = list(Counter(basket).values())
    groups = []

    # formation of groups
    while len(frequency):
        groups.append(len(frequency))
        frequency = [book - 1 for book in frequency if (book - 1) != 0]

    # replacing all (5, 3)s with (4, 4)s
    while 5 in groups and 3 in groups:
        groups[groups.index(5)] = 4
        groups[groups.index(3)] = 4
    
    return sum([round(PRICES[group], 2) * 100 for group in groups])
