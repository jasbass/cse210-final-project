from game.actions.action import Action
from game.sprites.point import Point

class HandleHorizontalCollisionsAction(Action):
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast):
        for player in cast['player']:
            for bush in cast['bushes']:
                if self._physics_service.is_collision(player, bush):

                    player_velocity_x = player.get_velocity().get_x()

                    if player_velocity_x != 0:
                        if player_velocity_x > 0:
                            x = bush.get_left_edge() - bush.get_width()
                            y = player.get_position().get_y()
                            player.set_position(Point(x, y))

                        if player_velocity_x < 0:
                            x = bush.get_right_edge()
                            y = player.get_position().get_y()
                            player.set_position(Point(x, y))           