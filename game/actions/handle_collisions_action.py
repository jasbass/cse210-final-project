from game.actions.action import Action
from game.sprites.sprite import Sprite
from game.sprites.player import Player
from game.sprites.bush import Bush
from game.sprites.point import Point
from game import constants

class HandleCollisionsAction(Action):
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast):
        for player in cast['player']:
            for bush in cast['bushes']:
                if self._physics_service.is_collision(player, bush):
                    player_velocity = player.get_velocity()
                    player_velocity_y = player_velocity.get_y()
                    player_velocity_x = player_velocity.get_x()

                    if player_velocity_y > 0:
                        x = player.get_position().get_x()
                        y = bush.get_top_edge() - bush.get_height()
                        player.set_position(Point(x, y))

                    if player_velocity_y < 0:
                        x = player.get_position().get_x()
                        y = bush.get_bottom_edge()
                        player.set_position(Point(x, y))

                    if player_velocity_x > 0:
                        x = bush.get_left_edge() - bush.get_width()
                        y = player.get_position().get_y()
                        player.set_position(Point(x, y))

                    if player_velocity_x < 0:
                        x = bush.get_right_edge()
                        y = player.get_position().get_y()
                        player.set_position(Point(x, y))