import raylibpy
from game.actions.action import Action
from game.sprites.sprite import Sprite
from game.sprites.point import Point
from game import constants

class CheckDeathsAction(Action):
    def __init__(self, physics_service):
        self._physics_service = physics_service

    def execute(self, cast):
        for player in cast['player']:
            for enemy in cast['enemies']:

                if enemy.get_direction() == 'right':
                    enemy_position = enemy.get_position()
                    vision = Sprite()
                    vision_x = enemy_position.get_x()
                    vision_y = enemy_position.get_y()
                    vision.set_position(Point(vision_x, vision_y))
                    vision.set_width(constants.MAX_X - vision_x)
                    vision.set_height(enemy.get_height())
                    if self._physics_service.is_collision(vision, player):
                        delete_player = True
                        for bush in cast['bushes']:
                            if self._physics_service.is_collision(vision, bush):
                                if (bush.get_position().get_x() - enemy_position.get_x()) < (player.get_position().get_x() - enemy_position.get_x()):
                                    delete_player = False
                        if delete_player:
                            if player in cast['player']:
                                cast['player'].remove(player)

                if enemy.get_direction() == 'left':
                    enemy_position = enemy.get_position()
                    vision = Sprite()
                    vision_x = 0
                    vision_y = enemy_position.get_y()
                    vision.set_position(Point(vision_x, vision_y))
                    vision.set_width(enemy_position.get_x() + enemy.get_width())
                    vision.set_height(enemy.get_height())
                    if self._physics_service.is_collision(vision, player):
                        delete_player = True
                        for bush in cast['bushes']:
                            if self._physics_service.is_collision(vision, bush):
                                if (enemy_position.get_x() - bush.get_position().get_x()) < (enemy_position.get_x() - player.get_position().get_x()):
                                    delete_player = False
                        if delete_player:
                            if player in cast['player']:
                                cast['player'].remove(player)

                if enemy.get_direction() == 'up':
                    enemy_position = enemy.get_position()
                    vision = Sprite()
                    vision_x = enemy_position.get_x()
                    vision_y = 0
                    vision.set_position(Point(vision_x, vision_y))
                    vision.set_width(enemy.get_width())
                    vision.set_height(enemy_position.get_y() + enemy.get_height())
                    if self._physics_service.is_collision(vision, player):
                        delete_player = True
                        for bush in cast['bushes']:
                            if self._physics_service.is_collision(vision, bush):
                                if (enemy_position.get_y() - bush.get_position().get_y()) < (enemy_position.get_y() - player.get_position().get_y()):
                                    delete_player = False
                        if delete_player:
                            if player in cast['player']:
                                cast['player'].remove(player)

                if enemy.get_direction() == 'down':
                    enemy_position = enemy.get_position()
                    vision = Sprite()
                    vision_x = enemy_position.get_x()
                    vision_y = enemy_position.get_y()
                    vision.set_position(Point(vision_x, vision_y))
                    vision.set_width(enemy.get_width())
                    vision.set_height(constants.MAX_Y - vision_y)
                    if self._physics_service.is_collision(vision, player):
                        delete_player = True
                        for bush in cast['bushes']:
                            if self._physics_service.is_collision(vision, bush):
                                if (bush.get_position().get_y() - enemy_position.get_y()) < (player.get_position().get_y() - enemy_position.get_y()):
                                    delete_player = False
                        if delete_player:
                            if player in cast['player']:
                                cast['player'].remove(player)