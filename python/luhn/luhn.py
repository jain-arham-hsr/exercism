class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isdigit():
            return False
        verification_num = list(self.card_num)
        for digit in range(len(verification_num)-2, -1, -2):
            verification_num[digit] = int(verification_num[digit])*2
            if verification_num[digit] > 9:
                verification_num[digit] -= 9
        return True if sum(map(int, verification_num)) % 10 == 0 else False
