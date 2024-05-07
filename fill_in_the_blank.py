#Josh Herup
#CS333 Final Project - Fill In The Blank
#Erin Keith
#05/06/24
import random
from card import Card
from deck import Deck

class FillInTheBlank:
    def __init__(self):
        self.correct_answers = 0
        self.total_questions = 0

    def generate_question(self, card):
        definition = card.definition
        term = card.term

        words = definition.split()

        blank_index = random.randint(0, len(words) - 1)
        blank_word = words[blank_index]

        words[blank_index] = "______"

        question_with_blank = " ".join(words)

        return question_with_blank, term, blank_word

    def check_answer(self, user_answer, correct_answer):
        self.total_questions += 1

        if user_answer.lower() == correct_answer.lower():
            self.correct_answers += 1
            return True
        else:
            return False

    def get_score(self):
        if self.total_questions == 0:
            return 0.0
        else:
            return (self.correct_answers / self.total_questions) * 100