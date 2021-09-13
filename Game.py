# Create your Game class logic in here.
import phrase from phrasehunter
import random

class Game():
    def __init__(self):
        self.missed = 0
        self.phrases =  [Phrase("fly up the sky"),
                        Phrase("love butter bagels"),
                        Phrase("python is the game"),
                        Phrase("cybersecurity is hot"),
                        Phrase("corona virus ")]
        self.active_phrases = self.get_random_phrase()
        self.guesses = [" "]


    def get_random_phrase(self):
        return random.choice(self.phrases)


    def welcome(self):
        print(" Welcome to the game ")    
        print("\n")
        print("use your full IQ and guess the phrase, GOOD LUCK ")

    def start(self):
        self.welcome()
        while self.missed < 5 and not self.active_phrases.check_complete(self.guesses):
            print("Wrong guess")
            self.active_phrases.display(self.guesses)
            print("\n")
            self.user_guess = self.get_guess()
            self.guesses.append(self.user_guess)
            self.active_phrases.check_guess(self.user_guess)
            if not self.active_phrasese.check_guess(self.user_guess):
                self.missed += 1
        self.end_game()


    def get_guess(self):
        return input("Type the letter you think of")


    def end_game(self):
        if self.missed == 5:
            print("You have used all the attempts, good luck next time")
        else:
            print("YOU HAVE WON. CONGRATS !!!!!")




            





