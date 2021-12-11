from game.sprites.sprite import Sprite
from game.sprites.point import Point
from game import constants
import raylibpy

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.set_image(constants.IMAGE_HERO)
        self.set_position(Point(x * constants.TILESIZE, y * constants.TILESIZE))
        self.set_width(constants.TILESIZE - 4)
        self.set_height(constants.TILESIZE - 4)
        self._facing = 'up'
        self._left_animations = constants.IMAGES_HERO['left_animations']
        self._right_animations = constants.IMAGES_HERO['right_animations']
        self._up_animations = constants.IMAGES_HERO['up_animations']
        self._down_animations = constants.IMAGES_HERO['down_animations']
        self._animation_counter = 1

    def get_animation_counter(self):
        return self._animation_counter

    def set_animation_counter(self, value):
        self._animation_counter = value

    def get_direction(self):
        return self._facing

    def set_direction(self, direction):
        self._facing = direction

    def get_left_animations(self):
        return self._left_animations

    def get_right_animations(self):
        return self._right_animations

    def get_up_animations(self):
        return self._up_animations

    def get_down_animations(self):
        return self._down_animations
        
        