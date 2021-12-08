from game.actions.action import Action
from math import floor

class AnimateSpritesAction(Action):
    def __init__(self):
        pass

    def execute(self, cast):
        for player in cast['player']:
            self.animate(player)
        
        for enemy in cast['enemies']:
            self.animate(enemy)

    def animate(self, sprite):
        direction = sprite.get_direction()
        if direction == 'down':
            dy = sprite.get_velocity().get_y()
            images = sprite.get_down_animations()
            if dy == 0:
                image = images[0] 
            else:
                animation_counter = sprite.get_animation_counter()
                image = images[floor(animation_counter)]
                animation_counter += 0.1
                if animation_counter >= 3:
                    animation_counter = 1
                sprite.set_animation_counter(animation_counter)
            sprite.set_image(image)

        if direction == 'up':
            dy = sprite.get_velocity().get_y()
            images = sprite.get_up_animations()
            if dy == 0:
                image = images[0] 
            else:
                animation_counter = sprite.get_animation_counter()
                image = images[floor(animation_counter)]
                animation_counter += 0.1
                if animation_counter >= 3:
                    animation_counter = 1
                sprite.set_animation_counter(animation_counter)
            sprite.set_image(image)

        if direction == 'left':
            dx = sprite.get_velocity().get_x()
            images = sprite.get_left_animations()
            if dx == 0:
                image = images[0] 
            else:
                animation_counter = sprite.get_animation_counter()
                image = images[floor(animation_counter)]
                animation_counter += 0.1
                if animation_counter >= 3:
                    animation_counter = 1
                sprite.set_animation_counter(animation_counter)
            sprite.set_image(image)

        if direction == 'right':
            dx = sprite.get_velocity().get_x()
            images = sprite.get_right_animations()
            if dx == 0:
                image = images[0] 
            else:
                animation_counter = sprite.get_animation_counter()
                image = images[floor(animation_counter)]
                animation_counter += 0.1
                if animation_counter >= 3:
                    animation_counter = 1
                sprite.set_animation_counter(animation_counter)
            sprite.set_image(image)