from game.sprites.sprite import Sprite
from game.sprites.point import Point
from game import constants

class Enemy(Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.set_position(Point(x * constants.TILESIZE, y * constants.TILESIZE))
        self.set_width(constants.TILESIZE)
        self.set_height(constants.TILESIZE)
        self._facing = 'right'

    def get_direction(self):
        return self._facing

    def set_direction(self, direction):
        self._facing = direction