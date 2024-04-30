#Josh Herup
#CS333 Final Project - Test Card
#Erin Keith
#04/28/24
import unittest
from card import Card

class TestCard(unittest.TestCase):
    def test_get_term(self):
        card = Card("term", "definition")
        self.assertEqual(card.get_term(), "term")
    
    def test_get_definition(self):
        card = Card("term", "definition")
        self.assertEqual(card.get_definition(), "definition")
