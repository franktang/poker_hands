from PokerCard import PokerCard


class PokerCardHand:
    cards = []

    def __init__(self, card_hand_input):
        self.cards.clear()
        for card in card_hand_input:
            self.cards.append(PokerCard(card))

    def get_card_hand_in_string(self):
        output_string = ""
        for card in self.cards:
            output_string += card.get_card_in_string()
        return output_string

    def is_high_card(self):

        for card in self.cards:
            if self.get_count_of_same_value(card.value) > 1:
                return False

        return True

    def get_count_of_same_value(self, search_value):
        count = 0
        for card in self.cards:
            if search_value == card.value:
                count += 1

        return count

    def is_pair(self):
        for card in self.cards:
            if self.get_count_of_same_value(card.value) == 2:
                return True

        return False

    def is_straight(self):
        sorted_card_list = sorted(self.cards, key=lambda card: card.rank)
        return self.is_continous(sorted_card_list)

    def is_continous(self, sorted_card_list):
        for index in range(1, len(sorted_card_list)):
            if sorted_card_list[index].rank - sorted_card_list[index-1].rank != 1:
                return False
        return True

