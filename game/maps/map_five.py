from game.maps.map import Map
from game.sprites.player import Player
from game.sprites.enemy import Enemy
from game.sprites.bush import Bush
from game.sprites.enemy_boundary import EnemyBoundary
from game.sprites.text_sprite import TextSprite
from game.sprites.ground import Ground
from game.sprites.point import Point
from game.sprites.door import Door
from game import constants

class MapFive(Map):
    def __init__(self) -> None:
        super().__init__()
        self._tilemap = [
        'BBBBBBBBBBBDDDBBBBBBBBBBB',
        'B.........B...B.........B',
        'B.........B...B.........B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.........B...B.........B',
        'B.........B...B.........B',
        'BBBBBBBBBBB.P.BBBBBBBBBBB',
        '...........BBB...........']

    def get_tilemap(self):
        return self._tilemap

    def generate_map(self, cast):
        for y, row in enumerate(self._tilemap):
            for x, column in enumerate(row):

                ground = Ground(x, y)
                cast['ground'].append(ground)

                if column == 'B':
                    bush = Bush(x, y)
                    cast['bushes'].append(bush)

                if column == 'P':
                    for player in cast['player']:
                        player.set_position(Point(x * constants.TILESIZE, y * constants.TILESIZE))

                if column == 'D':
                    door = Door(x, y)
                    cast['doors'].append(door)

            self._add_text_sprites(cast)
    
    def _add_text_sprites(self, cast):
        x = 180
        y = 300
        text = 'Halfway there!!! Keep it up you\'re almost out!!!'
        text_sprite = TextSprite(x, y, text)
        cast['text_sprites'].append(text_sprite)
                    

            