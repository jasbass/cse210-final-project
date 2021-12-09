import sys
from game.sprites.point import Point
import raylibpy

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        pass
        
    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if self.is_left_pressed():
            dx += -1
        
        if self.is_right_pressed():
            dx += 1
        
        if self.is_up_pressed():
            dy += -1
        
        if self.is_down_pressed():
            dy += 1

        direction = Point(dx, dy)
        return direction

    def is_left_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_A)

    def is_right_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_D)

    def is_up_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_W)

    def is_down_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_S)

    def window_should_close(self):
        return raylibpy.window_should_close()

    def get_mouse_pressed(self):
        return raylibpy.is_mouse_button_pressed(0)

    def get_mouse_pos(self):
        return raylibpy.get_mouse_position()
