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

class MapTwo(Map):
    def __init__(self) -> None:
        super().__init__()
        self._tilemap = [
        'BBBBBBBBBBBDDDBBBBBBBBBBB',
        'B.....G...B...B.........B',
        'B.....R.....R.......G...B',
        'B.......G.......G.......B',
        'B.........G.....R.G..B..B',
        'B..B...G.L.....G........B',
        'B........G.......G......B',
        'B.......B...............B',
        'B............B..........B',
        'B.......................B',
        'B........B......B.......B',
        'B.......................B',
        'B.......................B',
        'B.............Z.........B',
        'B..................G....B',
        'B.......................B',
        'B....G..................B',
        'B..............G........B',
        'BBBBBBBBBBB.P.BBBBBBBBBBB',
        '...........BBB...........']

    def get_tilemap(self):
        return self._tilemap

    def generate_map(self, cast):
        for y, row in enumerate(self._tilemap):
            for x, column in enumerate(row):

                ground = Ground(x, y)
                cast['ground'].append(ground)

                if column == 'G':
                    enemy_boundary = EnemyBoundary(x, y, 'clockwise_turn')
                    cast['enemy_boundaries'].append(enemy_boundary)

                if column == 'B':
                    bush = Bush(x, y)
                    cast['bushes'].append(bush)

                if column == 'P':
                    for player in cast['player']:
                        player.set_position(Point(x * constants.TILESIZE, y * constants.TILESIZE))

                if column == 'R':
                    enemy = Enemy(x, y, 'right')
                    cast['enemies'].append(enemy)

                if column == 'D':
                    door = Door(x, y)
                    cast['doors'].append(door)

                if column == 'Z':
                    bush = Bush(x, y)
                    enemy_boundary = EnemyBoundary(x, y, 'counterclockwise_turn')
                    cast['bushes'].append(bush)
                    cast['enemy_boundaries'].append(enemy_boundary)

                if column == 'L':
                    enemy = Enemy(x, y, 'left')
                    cast['enemies'].append(enemy)

            self._add_text_sprites(cast)
    
    def _add_text_sprites(self, cast):
        x = 200
        y = 200
        text = 'Ok, this is a bit harder, take your time.'
        text_sprite = TextSprite(x, y, text)
        cast['text_sprites'].append(text_sprite)
                    
