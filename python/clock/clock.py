class Clock:
    def __init__(self, hour, minute):
        self.hour, self.minute = divmod(minute, 60)
        self.hour = (self.hour + hour) % 24

    def __repr__(self):
        return "{hour:0=2d}:{minute:0=2d}".format(hour=self.hour, minute=self.minute)

    def __eq__(self, other):
        return str(Clock(self.hour, self.minute)) == str(Clock(other.hour, other.minute))

    def __add__(self, minutes):
        self.minute += minutes
        return Clock(self.hour, self.minute)

    def __sub__(self, minutes):
        self.minute -= minutes
        return Clock(self.hour, self.minute)
