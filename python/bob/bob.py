import re


def response(hey_bob):
    hey_bob = hey_bob.strip()
    if not hey_bob.split():
        return 'Fine. Be that way!'
    elif not re.search("[a-z]", hey_bob) and re.search("[A-Z]", hey_bob):
        if hey_bob.endswith("?"):
            return "Calm down, I know what I'm doing!"
        else:
            return 'Whoa, chill out!'
    elif hey_bob.endswith("?"):
        return 'Sure.'
    else:
        return 'Whatever.'
