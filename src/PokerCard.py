class PokerCard:
    value = "3"
    suit = "D"
    rank = 1
    rank_map = {
        "3": 1,
        "4": 2,
        "5": 3,
        "6": 4,
        "7": 5,
        "8": 6,
        "9": 7,
        "10": 8,
        "J": 9,
        "Q": 10,
        "K": 11,
        "A": 12,
        "2": 13
    }

    def __init__(self, card_input):
        self.value = card_input[0]
        self.suit = card_input[1]
        self.rank = self.rank_map[self.value]

    def get_card_in_string(self):
        return self.value + self.suit
