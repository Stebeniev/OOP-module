"""Module contains classes: GameOver, EnemyDown"""

from datetime import datetime


class GameOver(Exception):
    """Class GameOver"""

    def __init__(self, name, score):
        """Constructor accepts argument: player"""
        self.name = name
        self.score = score
        self.save_score()

    def save_score(self):
        """Method saves the game score"""


        with open("scores.txt", "a+", encoding="utf-8") as file:
            file.write(
                f"{self.name.capitalize()} : {self.score} : {datetime.now()} \n")


class EnemyDown(Exception):
    """Class EnemyDown"""
