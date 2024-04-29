#Josh Herup
#CS333 Final Project - Card
#Erin Keith
#04/28/24

class Card:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition
    
    def get_term(self):
        return self.term
    
    def get_definition(self):
        return self.definition