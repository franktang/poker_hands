class PokerCard:
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
    rank_map = {
        "2": 13,
        "A": 12,
        "K": 11,
        "Q": 10,
        "J": 9,
        "10": 8,
        "9": 7,
        "8": 6,
        "7": 5,
        "6": 4,
        "5": 3,
        "4": 2,
        "3": 1,
    }

    def __init__(self, card_input):
        self.value = card_input[:-1]
        self.suit = card_input[-1]
        self.straight_rank = self.straight_rank_map[self.value]
        self.rank = self.rank_map[self.value]

    def get_card_in_string(self):
        return self.value + self.suit
