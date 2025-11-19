from Model.Model import Model
from View.View import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def Start(self):
        randomWord, hiden, mistakes = self.model.StartGame()
        stickman = self.model.GetStickman()

        while True:
            self.view.GetWord(hiden)
            latters = self.view.Guess()

            if latters not in randomWord:
                mistakes += 1

                if mistakes >= len(stickman):
                    self.view.Loose(stickman[-1])
                    break
                self.view.PersonStage(stickman[mistakes])

            guess = ""
            for i in range (len(randomWord)):
                if randomWord[i] == latters:
                    guess += latters
                else:
                    guess += hiden[i]

            hiden = guess

            if hiden == randomWord:
                self.view.Won(randomWord)
                break