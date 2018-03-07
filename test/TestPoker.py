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