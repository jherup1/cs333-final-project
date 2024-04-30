#Josh Herup
#CS333 Final Project - Test Study Session
#Erin Keith
#04/28/24
import unittest
import os
from study_session import StudySession
from deck import Deck
from card import Card

class TestStudySession(unittest.TestCase):
    def setUp(self):
        self.deck = Deck("test_deck")
        self.deck.add_card("term1", "definition1")
        self.deck.add_card("term2", "definition2")
        self.deck.add_card("term3", "definition3")
        self.study_session = StudySession(self.deck)

    def tearDown(self):
        self.deck.delete_deck()

    def test_get_current_card(self):
        self.assertEqual(self.study_session.get_current_card(), None)

    def test_get_correct(self):
        self.assertEqual(self.study_session.get_correct(), 0)

    def test_get_incorrect(self):
        self.assertEqual(self.study_session.get_incorrect(), 0)

    def test_get_num_cards(self):
        self.assertEqual(self.study_session.get_num_cards(), 3)

    def test_get_remaining_cards(self):
        self.assertEqual(self.study_session.get_remaining_cards(), 3)

    def test_get_next_card(self):
        self.study_session.get_next_card()
        self.assertTrue(self.study_session.get_current_card().get_term() in ["term1", "term2", "term3"])
        self.assertTrue(self.study_session.get_current_card().get_definition() in ["definition1", "definition2", "definition3"])

    def test_check_answer(self):
        self.study_session.current_card = self.study_session.cards[0]
        self.assertTrue(self.study_session.check_answer("definition1"))
        self.assertEqual(self.study_session.get_correct(), 1)
        self.study_session.current_card = self.study_session.cards[1]
        self.assertFalse(self.study_session.check_answer("definition2"))
        self.assertEqual(self.study_session.get_incorrect(), 1)