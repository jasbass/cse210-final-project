from game.sprites.sprite import Sprite
from game.sprites.point import Point
from game import constants

class EnemyBoundary(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.set_position(Point(x * constants.TILESIZE, y * constants.TILESIZE))
        self.set_velocity(Point(0,0))
        self.set_width(constants.TILESIZE)
        self.set_height(constants.TILESIZE)