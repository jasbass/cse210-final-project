from game.sprites.sprite import Sprite
from game.sprites.point import Point
from game import constants

class EnemyBoundary(Sprite):
    def __init__(self, x, y, collision):
        super().__init__()
        self.set_position(Point(x * constants.TILESIZE, y * constants.TILESIZE))
        self.set_velocity(Point(0,0))
        self.set_width(constants.TILESIZE)
        self.set_height(constants.TILESIZE)
        # Collision types, clockwise_turn, counterclockwise_turn, full_turn
        self._collision = collision

    def set_collision(self, collision):
        self._collision = collision

    def get_collision(self):
        return self._collision