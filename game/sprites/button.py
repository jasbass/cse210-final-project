from game.sprites.sprite import Sprite
from game.sprites.point import Point
from game import constants

class Button(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.set_image(constants.IMAGE_BUTTON)
        self.set_position(Point(x, y))
        self.set_width(constants.BUTTON_WIDTH)
        self.set_height(constants.BUTTON_HEIGHT)
        self._pressed = False

    def set_pressed(self, bool):
        self._pressed = bool

    def is_pressed(self):
        return self._pressed