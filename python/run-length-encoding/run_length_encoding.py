def decode(string):
    res = ""
    cursor = 0
    repetitions = 1
    prev_char = ""
    while cursor < len(string):
        char = string[cursor]
        if char.isdigit():
            if prev_char.isdigit():
                repetitions = 10 * repetitions + int(char)
            else:
                repetitions = int(char)
        else:
            res += repetitions * char
            repetitions = 1
        prev_char = char
        cursor += 1
    return res


def encode(string):
    res = ""
    cursor = 0
    repetitions = 0
    if len(string) > 0:
        prev_char = string[0]
    else:
        return ""
    while cursor < len(string):
        char = string[cursor]
        if char == prev_char:
            repetitions += 1
        else:
            if repetitions > 1:
                res += str(repetitions) + prev_char
            else:
                res += prev_char
            repetitions = 1
        prev_char = char
        cursor += 1
    if repetitions > 1:
        res += str(repetitions) + prev_char
    else:
        res += prev_char
    return res
