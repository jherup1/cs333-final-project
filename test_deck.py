#Josh Herup
#CS333 Final Project - Test Deck
#Erin Keith
#04/28/24
import unittest
import os
from deck import Deck
from card import Card

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck("test_deck")

    def test_add_card(self):
        self.deck.add_card("term1", "definition1")
        self.deck.add_card("term2", "definition2")
        self.deck.add_card("term3", "definition3")
        self.deck.add_card("term4", "definition4")
        self.assertEqual(self.deck.get_card("term4").get_term(), "term4")
        self.assertEqual(self.deck.get_card("term4").get_definition(), "definition4")
    
    def test_remove_card(self):
        self.deck.remove_card("term2")
        self.assertEqual(self.deck.get_card("term2"), None)
    
    def test_edit_card(self):
        self.deck.edit_card("term3", "term5", "definition5")
        self.assertEqual(self.deck.get_card("term5").get_term(), "term5")
        self.assertEqual(self.deck.get_card("term5").get_definition(), "definition5")
    
    def test_get_card(self):
        self.assertEqual(self.deck.get_card("term1").get_term(), "term1")
        self.assertEqual(self.deck.get_card("term1").get_definition(), "definition1")
    
    def test_get_random_card(self):
        random_card = self.deck.get_random_card()
        self.assertTrue(random_card.get_term() in ["term1", "term4", "term5"])
        self.assertTrue(random_card.get_definition() in ["definition1", "definition4", "definitio5"])
    
    def test_get_all_cards(self):
        all_cards = self.deck.get_all_cards()
        self.assertEqual(len(all_cards), 3)
        self.assertEqual(all_cards[0].get_term(), "term1")
        self.assertEqual(all_cards[0].get_definition(), "definition1")
        self.assertEqual(all_cards[1].get_term(), "term4")
        self.assertEqual(all_cards[1].get_definition(), "definition4")
        self.assertEqual(all_cards[2].get_term(), "term5")
        self.assertEqual(all_cards[2].get_definition(), "definition5")

    def test_delete_deck(self):
        self.deck.delete_deck()
        self.assertFalse(os.path.exists(self.deck.filename))

if __name__ == "__main__": 
    unittest.main()