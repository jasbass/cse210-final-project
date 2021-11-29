from game.sprites.sprite import Sprite
from game import constants

class Enemy(Sprite):
    def __init__(self) -> None:
        self.set_width(constants.TILESIZE)
        self.set_height(constants.TILESIZE)