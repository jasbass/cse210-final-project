from game.sprites.sprite import Sprite
from game import constants

class EnemyBoundary(Sprite):
    def __init__(self):
        super().__init__()
        self.set_width(constants.TILESIZE)
        self.set_height(constants.TILESIZE)