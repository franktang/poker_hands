from PokerCard import PokerCard


class PokerCardHand:
    cards = []
    card_hand_input = ()
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

    @staticmethod
    def get_count_of_same_value_static(cards, search_value):
        count = 0
        for card in cards:
            if search_value == card.value:
                count += 1
        return count

    def get_count_of_same_suit(self, search_value):
        count = 0
        for card in self.cards:
            if search_value == card.suit:
                count += 1
        return count

    @staticmethod
    def get_count_of_same_suit_static(cards, search_value):
        count = 0
        for card in cards:
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

    @staticmethod
    def is_continous_static(sorted_card_list):
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

    @staticmethod
    def is_include_straight_pattern_static(sorted_card_list):
        include_straight_pattern = ("A10JQK")
        cards_value_string = ""
        for card in sorted_card_list:
            cards_value_string += card.value

        if cards_value_string in include_straight_pattern:
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
        strategy_list = [
            RoyalFlushStrategy(),
            FullHouseStrategy(),
            FlushStrategy(),
            StraightStrategy(),
            ThreeOfAKindStrategy(),
            PairStrategy(),
            HighCardStrategy()
        ]

        for strategy in strategy_list:
            if strategy.is_obey_this_strategy(self.cards):
                return strategy.category_name

        # if self.is_royal_flush():
        #     return "ROYAL_FLUSH"
        # elif self.is_full_house():
        #     return "FULL_HOUSE"
        # elif FlushStrategy().is_obey_this_strategy(self.cards):
        #     return FlushStrategy().category_name
        # elif StraightStrategy().is_obey_this_strategy(self.cards):
        #     return StraightStrategy().category_name
        # elif self.is_three_of_a_kind():
        #     return "THREE_OF_A_KIND"
        # elif self.is_pair():
        #     return "PAIR"
        # else:
        #     return "HIGH_CARD"


class CategoryStrategy:
    category_name = ''

    def determine_power(self):
        raise NotImplemented

    @staticmethod
    def is_obey_this_strategy(cards):
        raise NotImplemented


class RoyalFlushStrategy(CategoryStrategy):
    category_name = 'ROYAL_FLUSH'

    def determine_power(self):
        pass

    @staticmethod
    def is_obey_this_strategy(cards):
        return FlushStrategy.is_obey_this_strategy(cards) and StraightStrategy.is_obey_this_strategy(cards)

class FullHouseStrategy(CategoryStrategy):
    category_name = 'FULL_HOUSE'

    def determine_power(self):
        pass

    @staticmethod
    def is_obey_this_strategy(cards):
        return PairStrategy.is_obey_this_strategy(cards) and ThreeOfAKindStrategy.is_obey_this_strategy(cards)


class FlushStrategy(CategoryStrategy):
    category_name = 'FLUSH'

    def determine_power(self):
        pass

    @staticmethod
    def is_obey_this_strategy(cards):
        for card in cards:
            if PokerCardHand.get_count_of_same_suit_static(cards, card.suit) == 5:
                return True
        return False


class StraightStrategy(CategoryStrategy):
    category_name = 'STRAIGHT'

    def determine_power(self):
        pass

    @staticmethod
    def is_obey_this_strategy(cards):
        sorted_card_list = sorted(cards, key=lambda card: card.rank)
        return PokerCardHand.is_continous_static(sorted_card_list) or (PokerCardHand.is_include_straight_pattern_static(sorted_card_list))


class ThreeOfAKindStrategy(CategoryStrategy):
    category_name = 'THREE_OF_A_KIND'

    def determine_power(self):
        pass

    @staticmethod
    def is_obey_this_strategy(cards):
        for card in cards:
            if PokerCardHand.get_count_of_same_value_static(cards, card.value) == 3:
                return True
        return False


class PairStrategy(CategoryStrategy):
    category_name = 'PAIR'

    def determine_power(self):
        pass

    @staticmethod
    def is_obey_this_strategy(cards):
        for card in cards:
            if PokerCardHand.get_count_of_same_value_static(cards, card.value) == 2:
                return True
        return False


class HighCardStrategy(CategoryStrategy):
    category_name = 'HIGH_CARD'

    def determine_power(self):
        pass

    @staticmethod
    def is_obey_this_strategy(cards):
        return True