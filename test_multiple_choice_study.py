#Josh Herup
#CS333 Final Project - Test Multiple Choice Study
#Erin Keith
#05/06/24
import unittest
from deck import Deck
from card import Card
from multiple_choice_study import MultipleChoiceStudy

class TestMultipleChoiceStudy(unittest.TestCase):
    def setUp(self):
        self.deck = Deck("test")
        self.deck.add_card("term1", "definition1")
        self.deck.add_card("term2", "definition2")
        self.deck.add_card("term3", "definition3")
        self.deck.add_card("term4", "definition4")
        self.deck.add_card("term5", "definition5")
        self.deck.add_card("term6", "definition6")
        self.deck.add_card("term7", "definition7")
        self.deck.add_card("term8", "definition8")
        self.deck.add_card("term9", "definition9")
        self.deck.add_card("term10", "definition10")
        self.study = MultipleChoiceStudy(self.deck)

    def test_generate_choices(self):
        card = Card("term1", "definition1")
        options = self.study.generate_choices(card)
        self.assertEqual(len(options), 4)
        self.assertIn("definition1", options)

    def test_check_answer_correct(self):
        card = Card("term1", "definition1")
        choices = ["definition1", "definition2", "definition3", "definition4"]
        user_choice_index = 0
        result = self.study.check_answer(card, choices, user_choice_index)
        self.assertTrue(result)
        self.assertEqual(self.study.correct_answers, 1)
        self.assertEqual(self.study.total_questions, 1)

    def test_check_answer_incorrect(self):
        card = Card("term1", "definition1")
        choices = ["definition1", "definition2", "definition3", "definition4"]
        user_choice_index = 1
        result = self.study.check_answer(card, choices, user_choice_index)
        self.assertFalse(result)
        self.assertEqual(self.study.correct_answers, 0)
        self.assertEqual(self.study.total_questions, 1)

    def test_get_score(self):
        self.assertEqual(self.study.get_score(), 0.0)
        card = Card("term1", "definition1")
        choices = ["definition1", "definition2", "definition3", "definition4"]
        user_choice_index = 0
        self.study.check_answer(card, choices, user_choice_index)
        self.assertEqual(self.study.get_score(), 100.0)

    def tearDown(self):
        self.deck.delete_deck()