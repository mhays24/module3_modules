class BalloonTooFull(Exception):
    pass


class Balloon:
    def pump(self):
        self.amount += 3
        if self.amount > self.capacity:
            raise BalloonTooFull("Pop!")

    def release(self):
        self.amount -= 2
        self.amount = max(0, self.amount)


class SwordBalloon(Balloon):
    def __init__(self, capacity=5, amount=0):
        self.capacity = capacity
        self.amount = amount


class DogBalloon(Balloon):
    def __init__(self, capacity=7, amount=0):
        self.capacity = capacity
        self.amount = amount

class TriforceBalloon(Balloon):
    def __init__(self, capacity=11, amount=0):
        self.capacity = capacity
        self.amount = amount
