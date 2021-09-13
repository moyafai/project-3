# Create your Phrase class logic here.

class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()


    def display(self):
         for letter in self.active_phrases:
             if letter in self.guesses:
                 print(letter)
             else:
                 print("_ ") 


    def check_guess(self, guess):
        if guess in self.active_phrases:
            return True
        else:
            return False


    def check_complete(self):
        for letter in self.active_phrases:
            if letter not in self.active_phrases:
                return False
        else:
            return True                                       