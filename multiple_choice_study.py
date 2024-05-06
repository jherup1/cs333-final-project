#Josh Herup
#CS333 Final Project - Multiple Choice Study
#Erin Keith
#05/06/24
import random
from deck import Deck
from card import Card

class MultipleChoiceStudy:
    def __init__(self, deck, num_choices=4):
        self.deck = deck
        self.num_choices = num_choices
        self.correct_answers = 0
        self.total_questions = 0

    def generate_choices(self, card):
        correct_answer = card.definition
        choices = [correct_answer]

        while len(choices) < self.num_choices:
            random_card = self.deck.get_random_card()
            random_choice = random_card.definition
            if random_choice not in choices:
                choices.append(random_choice)

        random.shuffle(choices)
        
        return choices

    def check_answer(self, card, choices, user_choice_index):
        self.total_questions += 1
        correct_answer = card.definition
        user_choice = choices[user_choice_index]

        if user_choice == correct_answer:
            self.correct_answers += 1
            return True
        else:
            return False

    def get_score(self):
        if self.total_questions == 0:
            return 0.0
        else:
            return self.correct_answers / self.total_questions * 100
