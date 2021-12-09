from game.actions.action import Action
from game.sprites.sprite import Sprite
from game.sprites.point import Point

class CheckButtonsAction():
    def __init__(self, physics_service, input_service):
        self._physics_service = physics_service
        self._input_service = input_service

    def execute(self, cast):
        if self._input_service.get_mouse_pressed():
            x, y = self._input_service.get_mouse_pos()
            mouse_hitbox = Sprite()
            mouse_hitbox.set_position(Point(x, y))
            mouse_hitbox.set_width(1)
            mouse_hitbox.set_height(1)
            for button in cast['buttons']:
                if self._physics_service.is_collision(mouse_hitbox, button):
                    button.set_pressed(True)