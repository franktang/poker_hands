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

    def is_high_card(self):

        for card in self.card:
            if self.get_count_of_same_value(card.value) > 1:
                return False

        return True

    def get_count_of_same_value(self, search_value):
        count = 0
        for card in self.card:
            if search_value == card.value:
                count += 1

        return count

    def is_pair(self):
        for card in self.card:
            if self.get_count_of_same_value(card.value) == 2:
                return True

        return False
