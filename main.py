import random
from game import constants
from game.director import Director
from game.sprites.sprite import Sprite
from game.sprites.point import Point
from game.sprites.player import Player
from game.actions.draw_sprites_action import DrawSpritesAction
from game.actions.control_sprites_action import ControlSpritesAction
from game.actions.move_sprites_action import MoveSpritesAction
from game.actions.handle_collisions_action import HandleCollisionsAction
from game.interface.input_service import InputService
from game.interface.output_service import OutputService
from game.interface.physics_service import PhysicsService
from game.interface.audio_service import AudioService
# from game.brick import Brick


def main():

    # create the cast {key: tag, value: list}
    cast = {}
    player = Player(10, 10)
    player.set_velocity(Point(0,0))
    cast['player'] = []
    cast['enemy_boundaries'] = []
    cast['bushes'] = []
    cast['enemies'] = []


#Players, enemies, bushes, boundaries
    
    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_sprites_action = DrawSpritesAction(output_service)
    control_sprites_action = ControlSpritesAction(input_service)
    move_sprites_action = MoveSpritesAction()
    handle_collisions_action = HandleCollisionsAction(physics_service, audio_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_sprites_action]
    script["update"] = [move_sprites_action, handle_collisions_action]
    script["output"] = [draw_sprites_action]



    # Start the game
    output_service.open_window("Game")
    audio_service.start_audio()

    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()