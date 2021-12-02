from game.actions.action import Action
from game.sprites.point import Point

class HandleVerticalCollisionsAction(Action):
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast):
        for player in cast['player']:
            for bush in cast['bushes']:
                if self._physics_service.is_collision(player, bush):

                    player_velocity_y = player.get_velocity().get_y()


                    if player_velocity_y != 0:
                        if player_velocity_y > 0:
                            x = player.get_position().get_x()
                            y = bush.get_top_edge() - bush.get_height()
                            player.set_position(Point(x, y))

                        if player_velocity_y < 0:
                            x = player.get_position().get_x()
                            y = bush.get_bottom_edge()
                            player.set_position(Point(x, y))
                        