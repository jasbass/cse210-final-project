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

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._keep_playing = True
        
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        self.create_map(MapOne())

        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            if len(self._cast["player"]) == 0:
                # Game over
                self._game_over_screen()

            if raylibpy.window_should_close():
                self._keep_playing = False

    def create_map(self, map):
        tilemap = map.get_tilemap()
        for y, row in enumerate(tilemap):
            for x, column in enumerate(row):

                if column == 'G':
                    enemy_boundary = EnemyBoundary(x, y)
                    self._cast['enemy_boundaries'].append(enemy_boundary)
                if column == 'B':
                    bush = Bush(x, y)
                    self._cast['bushes'].append(bush)
                if column == 'P':
                    player  = Player(x, y)
                    self._cast['player'].append(player)
                if column == 'E':
                    enemy = Enemy(x, y)
                    self._cast['enemies'].append(enemy)


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)

    def _game_over_screen(self):
        print('Game Over')