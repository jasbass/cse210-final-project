from game.sprites.sprite import Sprite
from game.sprites.point import Point
from game import constants

class TextSprite(Sprite):
    def __init__(self, x, y, text):
        super().__init__()
        self.set_position(Point(x,y))
        self.set_text(text)

    