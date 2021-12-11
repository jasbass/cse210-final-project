from game.sprites.sprite import Sprite
from game.sprites.point import Point
from game import constants

class Enemy(Sprite):
    def __init__(self, x, y, direction) -> None:
        super().__init__()
        self.set_image(constants.IMAGES_ENEMY['down_animations'][0])
        self.set_position(Point(x * constants.TILESIZE, y * constants.TILESIZE))
        self.set_width(constants.TILESIZE)
        self.set_height(constants.TILESIZE)
        self.set_first_movement(direction)
        self._left_animations = constants.IMAGES_ENEMY['left_animations']
        self._right_animations = constants.IMAGES_ENEMY['right_animations']
        self._up_animations = constants.IMAGES_ENEMY['up_animations']
        self._down_animations = constants.IMAGES_ENEMY['down_animations']
        self._animation_counter = 1

    def set_first_movement(self, direction):
        if direction == 'right':
            self.set_velocity(Point(constants.ENEMY_SPEED, 0))

        if direction == 'left':
            self.set_velocity(Point(-constants.ENEMY_SPEED, 0))

        if direction == 'up':
            self.set_velocity(Point(0, -constants.ENEMY_SPEED))

        if direction == 'down':
            self.set_velocity(Point(0, constants.ENEMY_SPEED))

        self.set_direction(direction)

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