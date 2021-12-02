from game.actions.action import Action
from game.sprites.point import Point

class MoveSpritesHorizontalAction(Action):
    def __init__(self):
        pass

    def execute(self, cast):
        for group in cast.values():
            for sprite in group:
                position = sprite.get_position()
                x = position.get_x()
                y = position.get_y() 
                dx = sprite.get_velocity().get_x()
                sprite.set_position(Point(x + dx, y))
