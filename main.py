#Josh Herup
#CS333 Final Project - Main
#Erin Keith
#04/28/24
from deck import Deck
from card import Card
from study_session import StudySession
from multiple_choice_study import MultipleChoiceStudy
import os
import time

def list_decks():
    for deck in os.listdir("decks"):
        print(deck.split(".")[0])

def deck_editor(deck_name):
    deck = Deck(deck_name)
    user_choice_edit = ""
    while user_choice_edit != "0":
        print("Options:")
        print("0: Exit deck editor")
        print("1: Add a card")
        print("2: Remove a card")
        print("3: Edit a card")
        print("Please enter the number of the option you would like to select:")
        user_choice_edit = input()
        if user_choice_edit == "0":
            print("Goodbye!")
        elif user_choice_edit == "1":
            print("Please enter the term of the card you would like to add:")
            term = input()
            print("Please enter the definition of the card you would like to add:")
            definition = input()
            deck.add_card(term, definition)
            print("Card added successfully!")
        elif user_choice_edit == "2":
            print("Please enter the term of the card you would like to remove:")
            term = input()
            deck.remove_card(term)
            print("Card removed successfully!")
        elif user_choice_edit == "3":
            print("Please enter the term of the card you would like to edit:")
            term = input()
            print("Please enter the new term of the card:")
            new_term = input()
            print("Please enter the new definition of the card:")
            new_definition = input()
            deck.edit_card(term, new_term, new_definition)
            print("Card edited successfully!")
        else:
            print("Invalid input. Please try again.")

def main():
    user_choice = ""
    while user_choice != "0":
        print("Welcome to the Flashcard Study App!")
        print("Options:")
        print("0: Exit")
        print("1: Create a new deck")
        print("2: Study an existing deck")
        print("3: Start a multiple choice study session")
        print("4: View all decks")
        print("5: View specific deck")
        print("6: Edit a deck")
        print("7: Delete a deck")
        print("Please enter the number of the option you would like to select:")
        user_choice = input()
        if user_choice == "0":
            print("Goodbye!")
            break
        if user_choice == "1":
            print("Please enter the name of the deck you would like to create:")
            deck_name = input()
            deck = Deck(deck_name)
            deck_editor(deck_name)
            print("Deck created successfully!")
        elif user_choice == "2":
            print("Please enter the name of the deck you would like to study. Here are the available decks:")
            list_decks()
            deck_name = input()
            deck = Deck(deck_name)
            session = StudySession(deck)
            print("Welcome to the study session! Here is your first card:")
            print(session.get_next_card().get_term())
            print("Please enter your answer:")
            answer = input()
            if session.check_answer(answer):
                print("Correct!")
            else:
                print("Incorrect.")
            user_choice_study = ""
            while user_choice_study != "0":
                print("Options:")
                print("0: Exit study session")
                print("1: Get next card")
                print("2: Get number of correct answers")
                print("3: Get number of incorrect answers")
                print("4: Get number of remaining cards")
                print("Please enter the number of the option you would like to select:")
                user_choice_study = input()
                if user_choice_study == "0":
                    print("Goodbye!")
                elif user_choice_study == "1":
                    print(session.get_next_card().get_term())
                    print("Please enter your answer:")
                    answer = input()
                    if session.check_answer(answer):
                        print("Correct!")
                    else:
                        print("Incorrect.")
                elif user_choice_study == "2":
                    print(session.get_correct())
                elif user_choice_study == "3":
                    print(session.get_incorrect())
                elif user_choice_study == "4":
                    print(session.get_remaining_cards())
                else:
                    print("Invalid input. Please try again.")
                
                if not session.get_remaining_cards():
                    print("You have completed the study session! Here are your results:")
                    print(f"Correct: {session.get_correct()}")
                    print(f"Incorrect: {session.get_incorrect()}")
                    time.sleep(2)
                    break
        elif user_choice == "3":
            print("Please enter the name of the deck you would like to study. Here are the available decks:")
            list_decks()
            deck_name = input()
            deck = Deck(deck_name)
            session = MultipleChoiceStudy(deck)
            for card in deck.cards:
                choices = session.generate_choices(card)
                print(f"Question: {card.term}")
                for i, choice in enumerate(choices):
                    print(f"{i+1}. {choice}")
                user_choice_index = int(input("Enter the number of the correct answer: ")) - 1
                if session.check_answer(card, choices, user_choice_index):
                    print("Correct!")
                else:
                    print("Incorrect.")
            print(f"Your score: {session.get_score()}%")
        elif user_choice == "4":
            print("Here are all the available decks:")
            list_decks()
        elif user_choice == "5":
            print("Please enter the name of the deck you would like to view:")
            list_decks()
            deck_name = input()
            deck = Deck(deck_name)
            print(deck.get_all_cards())
        elif user_choice == "6":
            print("Please enter the name of the deck you would like to edit:")
            list_decks()
            deck_name = input()
            deck_editor(deck_name)
        elif user_choice == "7":
            print("Please enter the name of the deck you would like to delete:")
            list_decks()
            deck_name = input()
            deck = Deck(deck_name)
            deck.delete_deck()
            print("Deck deleted successfully!")
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()