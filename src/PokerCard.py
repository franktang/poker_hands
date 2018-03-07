class PokerCard:
    value = 3
    suit = 'D'

    def __init__(self, card_input):
        self.value = card_input[0]
        self.suit = card_input[1]

    def get_card_in_string(self):
        return self.value + self.suit
