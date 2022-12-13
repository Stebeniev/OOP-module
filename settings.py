"""Module contains program settings and class PlayerMove"""
from enum import IntEnum

PLAYER_LIVES = 3
ALLOWED_ATTACK = 3
LEVEL = 1


class PlayerMove(IntEnum):
    """Class PlayerMove"""
    WIZARD = 1
    WARRIOR = 2
    ROBBER = 3


settings = {"/start", "/show scores", "/help", "/exit"}




