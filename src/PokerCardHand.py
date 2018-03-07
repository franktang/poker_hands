from PokerCard import PokerCard


class PokerCardHand:
    card = []
    def __init__(self, card_hand_input):
        self.card.clear()
        for card in card_hand_input:
            self.card.append(PokerCard(card))


    def get_card_hand_in_string(self):
        output_string = ""
        for card in self.card:
            output_string += card.get_card_in_string()
        return output_string