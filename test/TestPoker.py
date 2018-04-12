import unittest

from src.PokerCardHand import PokerCardHand
from src.PokerCard import PokerCard
from src.PokerCardHand import *


class TestPoker(unittest.TestCase):
    def test_happy_flow(self):
        self.assertTrue(True)

    def test_create_poker_card_with_input(self):
        card = PokerCard("AS")
        self.assertEqual(card.get_card_in_string(), "AS")

    def test_create_one_poker_card_hand_with_input_series(self):
        card_hand_input = ("AS", "3D", "3C", "JS", "QC")

        card_hand = PokerCardHand(card_hand_input)

        self.assertEqual("AS3D3CJSQC", card_hand.get_card_hand_in_string())

    def test_given_one_high_card_hand_input_when_check_is_high_card_should_return_true(self):
        card_hand_input = ("AS", "3D", "6C", "JS", "QC")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.determine_category()

        self.assertEqual(result, HighCardStrategy.category_name)

    def test_given_one_pair_card_hand_input_when_check_is_high_card_should_return_false(self):
        card_hand_input = ("AS", "3D", "3C", "JS", "QC")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.determine_category()

        self.assertNotEqual(HighCardStrategy.category_name, result)

    def test_given_one_pair_card_hand_input_when_check_is_pair_should_return_true(self):
        card_hand_input = ("AS", "3D", "3C", "JS", "QC")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.determine_category()

        self.assertEqual(PairStrategy.category_name, result)

    def test_given_three_of_a_kind_card_hand_input_when_check_is_pair_should_return_false(self):
        card_hand_input = ("AS", "3D", "3C", "3S", "QC")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.determine_category()

        self.assertNotEqual(PairStrategy.category_name, result)

    def test_given_normal_straight_card_hand_input_when_check_is_straight_should_return_true(self):
        card_hand_input = ("3S", "4D", "5C", "6S", "7C")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.determine_category()

        self.assertEqual(StraightStrategy.category_name, result)

    def test_given_A2345_straight_card_hand_input_when_check_is_straight_should_return_true(self):
        card_hand_input = ("AS", "2D", "3C", "4S", "5C")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.determine_category()

        self.assertEqual(StraightStrategy.category_name, result)

    def test_given_23456_straight_card_hand_input_when_check_is_straight_should_return_true(self):
        card_hand_input = ("6S", "2D", "3C", "4S", "5C")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.determine_category()

        self.assertEqual(StraightStrategy.category_name ,result)

    def test_given_10JQKA_straight_card_hand_input_when_check_is_straight_should_return_true(self):
        card_hand_input = ("10S", "JD", "QC", "KS", "AC")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.determine_category()

        self.assertEqual(StraightStrategy.category_name, result)

    def test_given_10JQKA_straight_card_hand_input_when_check_is_straight_should_return_true(self):
        card_hand_input = ("10S", "JD", "QC", "KS", "AC")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.determine_category()

        self.assertEqual(StraightStrategy.category_name, result)

    def test_given_three_of_a_kind_card_hand_input_when_check_is_three_of_a_kind_should_return_true(self):
        card_hand_input = ("AS", "3D", "3C", "3S", "QC")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.determine_category()

        self.assertEqual(ThreeOfAKindStrategy.category_name, result)

    def test_given_flush_card_hand_input_when_check_is_flush_should_return_true(self):
        card_hand_input = ("AS", "5S", "3S", "9S", "JS")
        card_hand = PokerCardHand(card_hand_input)
        self.assertEqual("FLUSH", card_hand.determine_category())

    def test_given_full_house_when_determine_category_return_full_house(self):
        card_hand_input = ("AC", "AD", "9D", "9S", "AS")
        card_hand = PokerCardHand(card_hand_input)
        self.assertEqual("FULL_HOUSE", card_hand.determine_category())

    def test_given_royal_flush_hand_input_when_determine_category_return_royal_flush(self):
        card_hand_input = ("AS", "2S", "4S", "3S", "5S")
        card_hand = PokerCardHand(card_hand_input)
        self.assertEqual("ROYAL_FLUSH", card_hand.determine_category())


if __name__ == '__main__':
    unittest.main(verbosity=2)
