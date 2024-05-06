#Josh Herup
#CS333 Final Project - Study Session
#Erin Keith
#04/28/24
import random
from card import Card
from deck import Deck

class StudySession:
    def __init__(self, deck):
        self.deck = deck
        self.cards = self.deck.get_all_cards()
        self.current_card = None
        self.correct = 0
        self.incorrect = 0

    def get_current_card(self):
        return self.current_card

    def get_correct(self):
        return self.correct

    def get_incorrect(self):
        return self.incorrect

    def get_num_cards(self):
        return len(self.cards)

    def get_remaining_cards(self):
        return len(self.cards)

    def get_next_card(self):
        if self.cards:
            self.current_card = self.deck.get_random_card()
            return self.current_card
        return None

    def check_answer(self, answer):
        if self.current_card.get_definition() == answer:
            self.correct += 1
            self.cards.remove(self.current_card)
            return True
        else:
            self.incorrect += 1
            return False