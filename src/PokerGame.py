from src.PokerCardHand import *

class PokerGame(object):

    category_rank = [RoyalFlushStrategy.category_name,
                     FullHouseStrategy.category_name,
                     FlushStrategy.category_name,
                     StraightStrategy.category_name,
                     ThreeOfAKindStrategy.category_name,
                     PairStrategy.category_name,
                     HighCardStrategy.category_name]

    @staticmethod
    def compare(card_hand, card_hand_2):
        player_1_rank = PokerGame.category_rank.index(card_hand.determine_category())
        player_2_rank = PokerGame.category_rank.index(card_hand_2.determine_category())

        if player_1_rank <= player_2_rank:
            return card_hand.get_card_hand_in_string()
        else:
            return card_hand_2.get_card_hand_in_string()