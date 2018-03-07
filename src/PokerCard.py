class PokerCard:
    suit = 3
    value = 'D'

    def __init__(self, card_input):
        self.suit = card_input[0]
        self.value = card_input[1]

    def get_card_in_string(self):
        return self.suit + self.value
