from time import sleep
from game.sprites.sprite import Sprite
from game.sprites.point import Point
from game.maps.map_one import MapOne
from game.sprites.enemy_boundary import EnemyBoundary
from game.sprites.player import Player
from game.sprites.bush import Bush
from game.sprites.enemy import Enemy
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
        self._change_map(self._maps[self._map_index])

        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            if len(self._cast["player"]) == 0:
                # Game over
                self._game_over_screen()
            
            for player in self._cast['player']:
                for door in self._cast['doors']:
                    if self._physics_service.is_collision(player, door):
                        self._get_next_map()

            if raylibpy.window_should_close():
                self._keep_playing = False

    def _get_next_map(self):
        self._map_index += 1
        if (len(self._maps) - 1) < self._map_index:
            self._keep_playing = False
            self._game_won_screen()
        else:
            self._change_map(self._maps[self._map_index])
        

    def _game_won_screen(self):
        pass

    def _change_map(self, map):
        map.clear_map(self._cast)
        map.generate_map(self._cast)

    def _run_game_loop(self):
        pass

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)

    def _game_over_screen(self):
        print('Game Over')