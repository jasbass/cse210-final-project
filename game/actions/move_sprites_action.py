from game.actions.action import Action
from game.sprites.sprite import Sprite
from game.sprites.point import Point

class MoveSpritesAction(Action):
    def __init__(self):
        pass

    def execute(self, cast):
        for group in cast.values():
            for sprite in group:
                position = sprite.get_position()
                x = position.get_x()
                y = position.get_y()
                velocity = sprite.get_velocity() 
                dx = velocity.get_x()
                dy = velocity.get_y()
                sprite.set_position(Point(x + dx, y + dy))