from time import sleep
from game.sprites.sprite import Sprite
from game.sprites.point import Point
from game.sprites.player import Player
from game.sprites.enemy_boundary import EnemyBoundary
from game.sprites.button import Button
from game.sprites.background import Background
from game.sprites.text_sprite import TextSprite
from game import constants
import raylibpy

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script, maps, physics_service):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._physics_service = physics_service
        self._maps = maps
        self._map_index = 0

        self._keep_playing = True
        
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        self._run_intro()
        self._change_map(self._maps[self._map_index])

        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            if len(self._cast["player"]) == 0:
                # Game over
                self._game_over_screen()
            
            self._check_map_change()

            if raylibpy.window_should_close():
                self._keep_playing = False

    def _check_map_change(self):
        for player in self._cast['player']:
                for door in self._cast['doors']:
                    if self._physics_service.is_collision(player, door):
                        self._get_next_map()

    def _run_intro(self):
        self._maps[0].clear_map(self._cast)
        intro_background = Background()
        intro_background.set_image(constants.IMAGE_INTRO_BACKROUND)
        self._cast['backgrounds'].append(intro_background)
        button = Button(50, 50)
        self._cast['buttons'].append(button)
        text_one = TextSprite(10, 10, 'Escape The Goblins!!!')
        text_two = TextSprite(60, 60, 'Play Game!')
        self._cast['text_sprites'].append(text_one)
        self._cast['text_sprites'].append(text_two)
        intro = True
        while intro:
            
            self._cue_action('output')
            self._cue_action('check_buttons')

            if button.is_pressed():
                intro = False
                self._map_index = 0
                player = Player(0,0)
                self._cast['player'] = [player]
                self._change_map(self._maps[self._map_index])

            if raylibpy.window_should_close():
                intro = False
                self._keep_playing = False

    def _get_next_map(self):
        self._map_index += 1
        if (len(self._maps) - 1) < self._map_index:
            self._game_won_screen()
        else:
            self._change_map(self._maps[self._map_index])
        

    def _game_won_screen(self):
        self._cast['player'].clear()
        self._maps[0].clear_map(self._cast)
        game_won_background = Background()
        game_won_background.set_image(constants.IMAGE_INTRO_BACKROUND)
        self._cast['backgrounds'].append(game_won_background)
        button = Button(50, 50)
        self._cast['buttons'].append(button)
        text_one = TextSprite(10, 10, 'Congratulations! You\'ve escaped!')
        text_two = TextSprite(60, 60, 'Play Again?')
        self._cast['text_sprites'].append(text_one)
        self._cast['text_sprites'].append(text_two)
        game_won = True
        while game_won:
            
            self._cue_action('output')
            self._cue_action('check_buttons')

            if button.is_pressed():
                game_won = False
                self._run_intro()

            if raylibpy.window_should_close():
                game_won = False
                self._keep_playing = False

    def _change_map(self, map):
        map.clear_map(self._cast)
        map.generate_map(self._cast)

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)

    def _game_over_screen(self):
        self._maps[self._map_index].clear_map(self._cast)
        intro_background = Background()
        intro_background.set_image(constants.IMAGE_GAME_OVER)
        self._cast['backgrounds'].append(intro_background)
        button = Button(50, 50)
        self._cast['buttons'].append(button)
        text_one = TextSprite(10, 10, 'Game Over! Make sure you don\'t get seen!')
        text_two = TextSprite(60, 60, 'Restart?')
        self._cast['text_sprites'].append(text_one)
        self._cast['text_sprites'].append(text_two)
        game_over = True
        while game_over:
            
            self._cue_action('output')
            self._cue_action('check_buttons')

            if button.is_pressed():
                game_over = False
                self._run_intro()

            if raylibpy.window_should_close():
                game_over = False
                self._keep_playing = False