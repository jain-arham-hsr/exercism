def rotate(text, key):
    res = ""
    for ch in text:
        if not ch.isalpha():
            res += ch
            continue
        dec = ord(ch)
        if dec < 91:
            first_alpha = 65
        else:
            first_alpha = 97
        res += chr((dec + key - first_alpha) % 26 + first_alpha)
    return res
