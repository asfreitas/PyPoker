import deck

class Player:
    def __init__(self):
        self.hand = []
        self.chips = 0

    def get_card1(self):
        return self.hand[0]

    def get_card2(self):
        return self.hand[1]

    def get_card1_x(self):
        return self.hand[0].x

    def get_card1_y(self):
        return self.hand[0].y

    def get_card2_x(self):
        return self.hand[1].x

    def get_card2_y(self):
        return self.hand[1].y
