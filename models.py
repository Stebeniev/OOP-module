"""Module contains classes Enemy, Player"""

from random import randint
from settings import PLAYER_LIVES, ALLOWED_ATTACK, PlayerMove
from exception import GameOver, EnemyDown



class Enemy:
    """Class Enemy"""

    def __init__(self, level):
        """Constructor accepts argument: level"""
        self.level = level
        self.lives = self.level

    @staticmethod
    def select_attack():
        """Method returns a random number"""
        return randint(1, 3)

    def decrease_lives(self):
        """Method changes the number of opponent's lives and raises an exception EnemyDown"""
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown


class Player:
    """Class Player"""

    def __init__(self, name):
        """Constructor accepts argument: name"""
        self.name = name
        self.lives = PLAYER_LIVES
        self.score = 0
        self.allowed_attacks = ALLOWED_ATTACK

    @staticmethod
    def fight(attack, defense):
        """Method returns the result of the attack/defense"""
        if attack == defense:
            return 0
        elif (attack == 1 and defense == 2) or \
                (attack == 2 and defense == 3) or \
                (attack == 3 and defense == 1):
            return 1
        else:
            return -1


    def decrease_lives(self):
        """Method changes the number of opponent's lives and raises an exception GameOver"""
        self.lives -= 1
        if self.lives == 0:
            raise GameOver(self.name, self.score)

    def attack(self, enemy_obj):
        """Method receives data from the console and calls the method fight"""
        attack = int(input('Make a choice to move: Choice 1(rock), 2(paper) or 3(scissors):- '))
        defence = enemy_obj.select_attack()
        result = self.fight(attack, defence)
        if result == 0:
            print("it's Draw")
            print("__________________________")
        elif result == 1:
            print("You attacked successfully!")
            print("__________________________")
            self.score += 1
            enemy_obj.decrease_lives()
        elif result == -1:
            print("You missed!")
            print("__________________________")
        print(f"Your score:", self.score)
        print(f"Your life:", self.lives)

    def defence(self, enemy_obj):
        """Method receives data from the console and calls the method fight"""
        defence = int(input('Make a choice to move: Choice 1(rock), 2(paper) or 3(scissors):- '))
        attack = enemy_obj.select_attack()
        result = self.fight(attack, defence)
        if result == 0:
            print("it's Draw")
            print("____________________________")
        elif result == 1:
            print("Enemy attacked successfully!")
            print("____________________________")
            self.decrease_lives()
        elif result == -1:
            print("You missed!!")
            print("____________________________")

