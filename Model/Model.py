import random


class Model:
    def __init__(self):
        pass

    words = ["infrastructure","communication","relationship","transmission","environmental","distribution","consideration","implementation","configuration","responsibility"]

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


    def GetStickman(self):
        return self.Person

    def StartGame(self):
        randomWord = random.choice(self.words)
        hiden  = "*" * len(randomWord)
        mistakes = 0

        return randomWord, hiden, mistakes

