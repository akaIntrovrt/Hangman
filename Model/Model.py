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
        attempts = int(10);
        mistakes = 0

        Person = \
        [
            """
            
            
            """,

            """
             0
            """,
            """
             0
             |
            """,
            """
             0
             |\\
            """,
            """
             0
            /|\\
            """,
            """
             0
            /|\\
            /
            """,
            """
             0
            /|\\
            / \\
            """
        ]


        while True:
            print("\nCurrent word: " + hiden)
            CorrectGuess = ""
            choice = input("Enter you guess: ")
            attempts -= 1;
            print("Your current attempts: " + str(attempts))

            if(choice not in randomWord):
                mistakes += 1
                if(mistakes >= len(Person)):
                    print(Person[-1])
                    print("You got hangmaned, shma")
                    break

                print (Person[mistakes])

            for i in range(len(randomWord)):
                if randomWord[i] == choice:
                    CorrectGuess += choice
                else:
                    CorrectGuess += hiden[i]

            hiden = CorrectGuess

            if(hiden == randomWord):
                print("Correct! Word was: " + randomWord)
                break

user = Model(Model.words)
user.StartGame()
