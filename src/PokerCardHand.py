from PokerCard import PokerCard


class PokerCardHand:
    cards = []
    include_straight_pattern = ("A10JQK")

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

    def get_count_of_same_suit(self, search_value):
        count = 0
        for card in self.cards:
            if search_value == card.suit:
                count += 1
        return count

    def get_count_of_same_value_or_suit(self, value_or_suit, search_value):
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
        return self.is_continous(sorted_card_list) or (self.is_include_straight_pattern(sorted_card_list))

    def is_continous(self, sorted_card_list):
        for index in range(1, len(sorted_card_list)):
            if sorted_card_list[index].rank - sorted_card_list[index-1].rank != 1:
                return False
        return True

    def is_include_straight_pattern(self, sorted_card_list):
        cards_value_string = ""
        for card in sorted_card_list:
            cards_value_string += card.value

        if cards_value_string in self.include_straight_pattern:
            return True
        return False

    def is_three_of_a_kind(self):
        for card in self.cards:
            if self.get_count_of_same_value(card.value) == 3:
                return True
        return False

    def is_flush(self):
        for card in self.cards:
            if self.get_count_of_same_suit(card.suit) == 5:
                return True
        return False

    def is_full_house(self):
        return self.is_pair() and self.is_three_of_a_kind()

    def is_royal_flush(self):
        return self.is_straight() and self.is_flush()

    def determine_category(self):
        if self.is_royal_flush():
            return "ROYAL_FLUSH"
        elif self.is_full_house():
            return "FULL_HOUSE"
        elif self.is_flush():
            return "FLUSH"
        elif self.is_straight():
            return "STRAIGHT"
        elif self.is_three_of_a_kind():
            return "THREE_OF_A_KIND"
        elif self.is_pair():
            return "PAIR"
        else:
            return "HIGH_CARD"


class CategoryStrategy:
    def determine_power(self):
        raise NotImplemented

    def is_obey_this_strategy(self):
        raise NotImplemented


class RoyalFlushStrategy(CategoryStrategy):
    def determine_power(self):
        pass
    def is_obey_this_strategy(self, pokehand):
        pass