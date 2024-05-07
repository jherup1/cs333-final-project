#Josh Herup
#CS333 Final Project - Test Fill In The Blank
#Erin Keith
#05/06/24
import unittest
from card import Card
from deck import Deck
from fill_in_the_blank import FillInTheBlank

class TestFillInTheBlank(unittest.TestCase):
    def setUp(self):
        self.deck = Deck("test")
        self.deck.add_card("apple", "A fruit that is red or green.")

    def test_generate_question(self):
        fill_in_the_blank = FillInTheBlank()
        question, term, answer = fill_in_the_blank.generate_question(self.deck.get_card("apple"))
        self.assertNotEqual(question, "A fruit that is red or green.")
        self.assertEqual(term, "apple")

    def test_check_answer(self):
        fill_in_the_blank = FillInTheBlank()
        self.assertTrue(fill_in_the_blank.check_answer("apple", "apple"))
        self.assertTrue(fill_in_the_blank.check_answer("Apple", "apple"))
        self.assertFalse(fill_in_the_blank.check_answer("banana", "apple"))
        self.assertFalse(fill_in_the_blank.check_answer("orange", "apple"))

    def test_get_score(self):
        fill_in_the_blank = FillInTheBlank()
        fill_in_the_blank.check_answer("apple", "apple")
        fill_in_the_blank.check_answer("Apple", "apple")
        fill_in_the_blank.check_answer("banana", "apple")
        fill_in_the_blank.check_answer("orange", "apple")
        self.assertEqual(fill_in_the_blank.get_score(), 50.0)

    def tearDown(self):
        self.deck.delete_deck()