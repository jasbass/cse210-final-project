from game.maps.map import Map
from game.sprites.player import Player
from game.sprites.enemy import Enemy
from game.sprites.bush import Bush
from game.sprites.enemy_boundary import EnemyBoundary
from game.sprites.ground import Ground
from game.sprites.point import Point
from game.sprites.door import Door
from game import constants

class MapSeven(Map):
    def __init__(self) -> None:
        super().__init__()
        self._tilemap = [
        'BBBBBBBBBBBDDBBBBBBBBBBBB',
        'B.........B...B.........B',
        'B.........B...B.........B',
        'B.........B...B.........B',
        'B.........B...B.........B',
        'B.........B...B.........B',
        'B.........B...B.........B',
        'B...BBB...B...B.........B',
        'B.....B...B...B.........B',
        'B....B....B...B.........B',
        'B...B.....B...B.........B',
        'B.........B...B.........B',
        'B.........B...B.........B',
        'B.........B...B.........B',
        'B.........B...B.........B',
        'B.........B...B.........B',
        'B.........B...B.........B',
        'B.........B.P.B.........B',
        'BBBBBBBBBBBBBBBBBBBBBBBBB']

    def get_tilemap(self):
        return self._tilemap

    def generate_map(self, cast):
        for y, row in enumerate(self._tilemap):
            for x, column in enumerate(row):

                ground = Ground(x, y)
                cast['ground'].append(ground)

                if column == 'G':
                    enemy_boundary = EnemyBoundary(x, y)
                    cast['enemy_boundaries'].append(enemy_boundary)

                if column == 'B':
                    bush = Bush(x, y)
                    cast['bushes'].append(bush)

                if column == 'P':
                    for player in cast['player']:
                        player.set_position(Point(x * constants.TILESIZE, y * constants.TILESIZE))

                if column == 'E':
                    enemy = Enemy(x, y)
                    cast['enemies'].append(enemy)

                if column == 'D':
                    door = Door(x, y)
                    cast['doors'].append(door)