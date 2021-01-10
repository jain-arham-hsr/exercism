import re


class PhoneNumber:

    def __init__(self, number):
        self.number = "".join(re.findall(r'\d+', number))[-10:]
        self.area_code = self.number[0:3]
        self.exchange_code = self.number[3:]
        if any([len(self.number) > 11,
                len(number) == 11 and not number.startswith("1"),
                re.search('[a-zA-Z]', number),
                self.area_code.startswith('0'),
                self.area_code.startswith('1'),
                self.exchange_code.startswith('0'),
                self.exchange_code.startswith('1')]):
            raise ValueError("Invalid Input")

    def pretty(self):
        return "(%s) %s-%s" % (self.area_code, self.exchange_code[0:3], self.exchange_code[3:])
