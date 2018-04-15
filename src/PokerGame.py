from src.PokerCardHand import *


class PokerGame:
    category_rank = [RoyalFlushStrategy.category_name,
                     FullHouseStrategy.category_name,
                     FlushStrategy.category_name,
                     StraightStrategy.category_name,
                     ThreeOfAKindStrategy.category_name,
                     PairStrategy.category_name,
                     HighCardStrategy.category_name]

    @staticmethod
    def compare(card_hand, card_hand_2):
        card_1_strategy = card_hand.get_strategy()
        card_2_strategy = card_hand_2.get_strategy()

        card_1_rank = PokerGame.category_rank.index(card_1_strategy.category_name)
        card_2_rank = PokerGame.category_rank.index(card_2_strategy.category_name)

        if card_1_rank == card_2_rank:
            card_1_power = card_1_strategy.determine_power(card_hand)
            card_2_power = card_2_strategy.determine_power(card_hand_2)
            if card_1_power == card_2_power:
                return "equal"
            elif card_1_power > card_2_power:
                return card_hand.get_card_hand_in_string()
            else:
                return card_hand_2.get_card_hand_in_string()
        elif card_1_rank < card_2_rank:
            return card_hand.get_card_hand_in_string()
        else:
            return card_hand_2.get_card_hand_in_string()
