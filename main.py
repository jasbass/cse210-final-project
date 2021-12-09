from game import constants
from game.director import Director
from game.sprites.player import Player
from game.actions.draw_sprites_action import DrawSpritesAction
from game.actions.control_sprites_action import ControlSpritesAction
from game.actions.move_sprites_vertical_action import MoveSpritesVerticalAction
from game.actions.move_sprites_horizontal_action import MoveSpritesHorizontalAction
from game.actions.handle_horizontal_collisions_action import HandleHorizontalCollisionsAction
from game.actions.handle_vertical_collisions_action import HandleVerticalCollisionsAction
from game.actions.animate_sprites_action import AnimateSpritesAction
from game.actions.update_enemies_action import UpdateEnemiesAction
from game.actions.check_deaths_action import CheckDeathsAction
from game.actions.check_buttons_action import CheckButtonsAction
from game.interface.input_service import InputService
from game.interface.output_service import OutputService
from game.interface.physics_service import PhysicsService
from game.interface.audio_service import AudioService
from game.maps.map_one import MapOne
from game.maps.map_two import MapTwo
from game.maps.map_three import MapThree
from game.maps.map_four import MapFour
from game.maps.map_five import MapFive
from game.maps.map_six import MapSix
from game.maps.map_seven import MapSeven
from game.maps.map_eight import MapEight
from game.maps.map_nine import MapNine
from game.maps.map_ten import MapTen

def main():

    # create the cast {key: tag, value: list}
    cast = {}
    cast['backgrounds'] = []
    cast['ground'] = []
    cast['enemy_boundaries'] = []
    cast['doors'] = []
    cast['bushes'] = []
    cast['buttons'] = []
    cast['text_sprites'] = []
    cast['enemies'] = []
    cast['player'] = []

    maps = [MapOne(), MapTwo(), MapThree(), MapFour(), MapFive(), MapSix(), MapSeven(), MapEight(), MapNine(), MapTen()]
    
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
    animate_sprites_action = AnimateSpritesAction()
    check_buttons_action = CheckButtonsAction(physics_service, input_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_sprites_action]

    script["update"] = [move_sprites_vertical_action, handle_vertical_collisions_action, 
        move_sprites_horizontal_action, handle_horizontal_collisions_action, update_enemies_action,
        check_deaths_action, animate_sprites_action]

    script["output"] = [draw_sprites_action]

    script["check_buttons"] = [check_buttons_action]

    # Start the game
    output_service.open_window("Game")
    audio_service.start_audio()

    director = Director(cast, script, maps, physics_service)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()