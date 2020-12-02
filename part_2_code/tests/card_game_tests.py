import unittest
from src.card import Card
from src.card_game import CardGame 

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("heart", 1)
        self.card2 = Card("spade", 7)
        self.game1 = CardGame()

    def test_check_for_ace_true(self):
         ace = self.game1.check_for_ace(self.card1)
         self.assertEqual(ace, True)

    def test_check_for_ace_false(self):
        ace = self.game1.check_for_ace(self.card2)
        self.assertEqual(ace, False)

    def test_highest_card(self):
        result = self.game1.highest_card(self.card1, self.card2)
        self.assertEqual(result, self.card2)

    def test_card_total(self):
        all_cards = []
        all_cards.append(self.card1)
        all_cards.append(self.card2)
        total = self.game1.cards_total(all_cards)
        self.assertEqual(total, "You have a total of 8")

