#Josh Herup
#CS333 Final Project - Test Deck
#Erin Keith
#04/28/24
import unittest
from deck import Deck
from card import Card

class TestDeck(unittest.TestCase):
    def test_add_card(self):
        deck = Deck()
        deck.add_card("term", "definition")
        self.assertEqual(deck.get_all_cards()[0].get_term(), "term")
        self.assertEqual(deck.get_all_cards()[0].get_definition(), "definition")
    
    def test_remove_card(self):
        deck = Deck()
        deck.add_card("term", "definition")
        deck.remove_card("term")
        self.assertEqual(deck.get_all_cards(), [])
    
    def test_get_card(self):
        deck = Deck()
        deck.add_card("term", "definition")
        self.assertEqual(deck.get_card("term").get_term(), "term")
        self.assertEqual(deck.get_card("term").get_definition(), "definition")
    
    def test_get_random_card(self):
        deck = Deck()
        deck.add_card("term", "definition")
        self.assertEqual(deck.get_random_card().get_term(), "term")
        self.assertEqual(deck.get_random_card().get_definition(), "definition")