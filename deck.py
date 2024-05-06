#Josh Herup
#CS333 Final Project - Deck
#Erin Keith
#04/28/24
from card import Card
import random
import json
import os

class Deck:
    def __init__(self, deck_name):
        # if os.path.exists(os.path.join("decks", f"{deck_name}.json")):
        #     raise Exception("Deck already exists.")
        self.name = deck_name
        self.filename = os.path.join("decks", f"{deck_name}.json")
        self.load_from_json()

    def add_card(self, term, definition):
        self.load_from_json()
        self.cards.append({"term": term, "definition": definition})
        self.save_to_json()

    def remove_card(self, term):
        self.load_from_json()
        for card in self.cards:
            if card["term"] == term:
                self.cards.remove(card)
        self.save_to_json()
        return

    def edit_card(self, term, new_term, new_definition):
        self.load_from_json()
        for card in self.cards:
            if card["term"] == term:
                card["term"] = new_term
                card["definition"] = new_definition
        self.save_to_json()
        return

    def get_card(self, term):
        self.load_from_json()
        for card in self.cards:
            if card["term"] == term:
                return Card(card["term"], card["definition"])
        return None

    def get_random_card(self):
        self.load_from_json()
        if self.cards:
            random_card = random.choice(self.cards)
            return Card(random_card["term"], random_card["definition"])

    def get_all_cards(self):
        self.load_from_json()
        return [Card(card["term"], card["definition"]) for card in self.cards]
    
    def delete_deck(self):
        os.remove(self.filename)
    
    def save_to_json(self):
        deck_folder = "decks"
        if not os.path.exists(deck_folder):
            os.makedirs(deck_folder)
        #print(self.filename)
        if os.path.exists(self.filename):
            #print("Deck already exists. Deleting deck.")
            self.delete_deck()
        with open(self.filename, "w") as json_file:
            #print("Saving deck to json.")
            json.dump({"cards": self.cards}, json_file, indent=4)

    def load_from_json(self):
        try:
            with open(self.filename, "r") as json_file:
                data = json.load(json_file)
                self.cards = data["cards"]
        except FileNotFoundError:
            self.cards = []