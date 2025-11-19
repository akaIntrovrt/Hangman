import random


class Model:
    def __init__(self, words):
        self.words = words

    words = ["infrastructure","communication","relationship","transmission","environmental","distribution","consideration","implementation","configuration","responsibility"]

    def StartGame(self):

        print("Enter '1' any time, if you want tip.")

        randomWord = random.choice(self.words)
        hiden = "*" * len(randomWord)
        countLen = len(randomWord)

        while True:
            CorrectGuess = ""
            choice = input("Enter you guess: ")
            for i in range(len(randomWord)):
                if randomWord[i] == choice:
                    CorrectGuess += choice
                else:
                    CorrectGuess += hiden[i]
            hiden = CorrectGuess

            if(hiden == randomWord):
                print("Correct!")
