from game.actions.action import Action
from game.sprites.point import Point
from game import constants

class UpdateEnemiesAction(Action):
    def __init__(self, physics_service):
        self._physics_service = physics_service

    def execute(self, cast):
        for enemy in cast['enemies']:
            for enemy_boundary in cast['enemy_boundaries']:
                if self._physics_service.is_collision(enemy, enemy_boundary):
                    self._turn_enemy_clockwise(enemy, enemy_boundary)
            for bush in cast['bushes']:
                if self._physics_service.is_collision(enemy, bush):
                    self._turn_enemy_clockwise(enemy, bush)

    def _turn_enemy_clockwise(self, enemy, object):
        
        direction = enemy.get_direction()
        if direction == 'left':
            x = object.get_right_edge()
            y = enemy.get_position().get_y()
            enemy.set_position(Point(x, y))
            enemy.set_velocity(Point(0,-constants.ENEMY_SPEED))
            enemy.set_direction('up')

        if direction == 'right':
            x = object.get_left_edge() - object.get_width()
            y = enemy.get_position().get_y()
            enemy.set_position(Point(x, y))
            enemy.set_velocity(Point(0, constants.ENEMY_SPEED))
            enemy.set_direction('down')

        if direction == 'up':
            x = enemy.get_position().get_x()
            y = object.get_bottom_edge()
            enemy.set_position(Point(x, y))
            enemy.set_velocity(Point(constants.ENEMY_SPEED, 0))
            enemy.set_direction('right')

        if direction == 'down':
            x = enemy.get_position().get_x()
            y = object.get_top_edge() - object.get_height()
            enemy.set_position(Point(x, y))
            enemy.set_velocity(Point(-constants.ENEMY_SPEED, 0))
            enemy.set_direction('left')
