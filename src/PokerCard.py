class PokerCard:
    value = "3"
    suit = "D"
    rank = 1
    straight_rank_map = {
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 1,
        "2": 2
    }

    def __init__(self, card_input):
        self.value = card_input[0]
        self.suit = card_input[1]
        self.rank = self.straight_rank_map[self.value]

    def get_card_in_string(self):
        return self.value + self.suit
