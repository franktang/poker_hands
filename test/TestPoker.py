import unittest

from PokerCardHand import PokerCardHand
from PokerCard import PokerCard


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

        result = card_hand.is_high_card()

        self.assertTrue(result)

    def test_given_one_pair_card_hand_input_when_check_is_high_card_should_return_false(self):
        card_hand_input = ("AS", "3D", "3C", "JS", "QC")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.is_high_card()

        self.assertFalse(result)

    def test_given_one_pair_card_hand_input_when_check_is_pair_should_return_true(self):
        card_hand_input = ("AS", "3D", "3C", "JS", "QC")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.is_pair()

        self.assertTrue(result)

    def test_given_three_of_a_kind_card_hand_input_when_check_is_pair_should_return_false(self):
        card_hand_input = ("AS", "3D", "3C", "3S", "QC")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.is_pair()

        self.assertFalse(result)

    def test_given_normal_straight_card_hand_input_when_check_is_straight_should_return_true(self):
        card_hand_input = ("3S", "4D", "5C", "6S", "7C")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.is_straight()

        self.assertTrue(result)

    def test_given_A2345_straight_card_hand_input_when_check_is_straight_should_return_true(self):
        card_hand_input = ("AS", "2D", "3C", "4S", "5C")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.is_straight()

        self.assertTrue(result)

    def test_given_23456_straight_card_hand_input_when_check_is_straight_should_return_true(self):
        card_hand_input = ("6S", "2D", "3C", "4S", "5C")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.is_straight()

        self.assertTrue(result)

    def test_given_10JQKA_straight_card_hand_input_when_check_is_straight_should_return_true(self):
        card_hand_input = ("10S", "JD", "QC", "KS", "AC")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.is_straight()

        self.assertTrue(result)

    def test_given_10JQKA_straight_card_hand_input_when_check_is_straight_should_return_true(self):
        card_hand_input = ("10S", "JD", "QC", "KS", "AC")
        card_hand = PokerCardHand(card_hand_input)

        result = card_hand.is_straight()

        self.assertTrue(result)

