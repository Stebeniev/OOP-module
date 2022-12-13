"""Main executive module of the program"""
from exception import GameOver, EnemyDown
from models import Enemy, Player


def play():
    """Program launch method"""
    name = input("Enter your name: ")
    if not str(name).isalpha():
        raise Exception("Name must be alphabetic")
    player = Player(name)
    level = 1
    enemy_obj = Enemy(level)
    while True:
        try:
            player.attack(enemy_obj)
            player.defence(enemy_obj)
        except EnemyDown:
            level += 1
            player.score += 5
            enemy_obj = Enemy(level)
            print("Win!")
            print(f"Name:- {player.name}\n"
                  f"Score:- {player.score}\n"
)





if __name__ == '__main__':
    try:
        print(f"Your score - {play()}")
    except GameOver:
        print("\nGame Over")
    except KeyboardInterrupt:
        pass
    finally:
        print("\nGood Bye!")

