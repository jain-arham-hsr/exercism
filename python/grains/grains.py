def square(number):
    if not 0 < number < 65:
        raise ValueError("Invalid Input")
    return 2 ** (number - 1)


def total():
    return (2 ** 64) - 1
