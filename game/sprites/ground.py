from game.sprites.sprite import Sprite
from game.sprites.point import Point
from game import constants
from random import randint

class Ground(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self._image = self.get_random_ground_image()
        self.set_image(self._image)
        self.set_position(Point(x * constants.TILESIZE, y * constants.TILESIZE))
        self.set_width(constants.TILESIZE)
        self.set_height(constants.TILESIZE)

    def get_random_ground_image(self):
        index = randint(0, 5)
        image = constants.IMAGES_GROUND[index]
        return image
