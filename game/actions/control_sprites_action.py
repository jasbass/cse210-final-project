from game.actions.action import Action
from game.sprites.point import Point
from game import constants

class ControlSpritesAction(Action):
    def __init__(self, input_service):
        self._input_service = input_service

    def execute(self, cast):
        direction = self._input_service.get_direction()
        x = direction.get_x()
        y = direction.get_y()
        dx = constants.PLAYER_SPEED * x
        dy = constants.PLAYER_SPEED * y
        for player in cast['player']:
            if dx > 0:
                player.set_direction('right')
            if dx < 0:
                player.set_direction('left')
            if dy > 0:
                player.set_direction('down')
            if dy < 0:
                player.set_direction('up')
            player.set_velocity(Point(dx, dy))