import re

def is_valid(isbn):
    isbn_pretty = isbn.replace("-", "")
    if len(isbn_pretty) != 10 or re.search('[a-zA-Z]', isbn_pretty[:-1]) or re.search('[^X0-9]', isbn_pretty[-1]):
        return False
    res = 0
    for x, i in zip(isbn_pretty, reversed(range(1, 11))):
        if x == "X":
            x = 10
        res += int(x)*i
    return res % 11 == 0
