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

        for current_card_index in range(len(self.card)):
            current_card_value = self.card[current_card_index].value
            if self.found_card_with_same_value(current_card_value, current_card_index+1):
                return False

        return True

    def found_card_with_same_value(self, search_value, start_index):
        for card in self.card[start_index:]:
            if search_value == card.value:
                return True
        return False
