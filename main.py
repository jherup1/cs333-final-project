#Josh Herup
#CS333 Final Project - Main
#Erin Keith
#04/28/24
from deck import Deck
from card import Card

def main():
    deck = Deck("test_deck")
    deck.add_card("term1", "definition1")
    deck.add_card("term2", "definition2")
    deck.add_card("term3", "definition3")
    deck.add_card("term4", "definition4")
    deck.remove_card("term2")
    deck.edit_card("term3", "term5", "definition5")
    deck.get_card("term5")
    deck.get_card("term5")
    deck.get_card("term1")
    deck.get_card("term1")
    deck.get_random_card()
    deck.delete_deck()

if __name__ == "__main__":
    main()