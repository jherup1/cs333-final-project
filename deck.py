#Josh Herup
#CS333 Final Project - Deck
#Erin Keith
#04/28/24
from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
    
    def add_card(self, term, definition):
        card = Card(term, definition)
        self.cards.append(card)
    
    def remove_card(self, term):
        for card in self.cards:
            if card.get_term() == term:
                self.cards.remove(card)
    
    def get_card(self, term):
        for card in self.cards:
            if card.get_term() == term:
                return card
    
    def get_random_card(self):
        return random.choice(self.cards)
    
    def get_all_cards(self):
        return self.cards