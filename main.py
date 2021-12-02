import random
from game import constants
from game.director import Director
from game.sprites.sprite import Sprite
from game.sprites.point import Point
from game.sprites.player import Player
from game.actions.draw_sprites_action import DrawSpritesAction
from game.actions.control_sprites_action import ControlSpritesAction
from game.actions.move_sprites_vertical_action import MoveSpritesVerticalAction
from game.actions.move_sprites_horizontal_action import MoveSpritesHorizontalAction
from game.actions.handle_horizontal_collisions_action import HandleHorizontalCollisionsAction
from game.actions.handle_vertical_collisions_action import HandleVerticalCollisionsAction
from game.actions.update_enemies_action import UpdateEnemiesAction
from game.actions.check_deaths_action import CheckDeathsAction
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
    cast['ground'] = []
    cast['enemy_boundaries'] = []
    cast['bushes'] = []
    cast['enemies'] = []
    cast['player'] = []
    
    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_sprites_action = DrawSpritesAction(output_service)
    control_sprites_action = ControlSpritesAction(input_service)
    move_sprites_vertical_action = MoveSpritesVerticalAction()
    move_sprites_horizontal_action = MoveSpritesHorizontalAction()
    handle_vertical_collisions_action = HandleVerticalCollisionsAction(physics_service, audio_service)
    handle_horizontal_collisions_action = HandleHorizontalCollisionsAction(physics_service, audio_service)
    update_enemies_action = UpdateEnemiesAction(physics_service)
    check_deaths_action = CheckDeathsAction(physics_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_sprites_action]

    script["update"] = [move_sprites_vertical_action, handle_vertical_collisions_action, 
        move_sprites_horizontal_action, handle_horizontal_collisions_action, update_enemies_action,
        check_deaths_action]

    script["output"] = [draw_sprites_action]

    # Start the game
    output_service.open_window("Game")
    audio_service.start_audio()

    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()