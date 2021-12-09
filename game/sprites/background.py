from game.sprites.sprite import Sprite
from game.sprites.point import Point
from game import constants

class Background(Sprite):
    def __init__(self):
        super().__init__()
        self.set_position(Point(0, 0))
        self.set_width(constants.MAX_X)
        self.set_height(constants.MAX_Y)