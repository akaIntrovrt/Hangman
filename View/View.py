class View:
    def GetWord(self, word):
        print(f"\nCurrent word: {word}")

    def PersonStage(self, stage):
        print(f"\nIncorrect! Current stage: {stage}")

    def Won(self, word):
        print(f"\nCorrect! Word is {word}")

    def Loose(self, stage):
        print(stage)
        print(f"\nYou got hangmened, shma")

    def Guess(self):
        return input(f"\nEnter your guess: ")

