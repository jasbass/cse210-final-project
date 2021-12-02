from game.maps.map import Map
from game.sprites.player import Player
from game.sprites.enemy import Enemy
from game.sprites.bush import Bush
from game.sprites.enemy_boundary import EnemyBoundary
from game.sprites.ground import Ground

class MapOne(Map):
    def __init__(self) -> None:
        super().__init__()
        self._tilemap = [
        'BBBBBBBBBBBBBBBBBBBBBBBBB',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B...GGGG................B',
        'BP.GE...G...............B',
        'B..G....G...............B',
        'B...GGGG....B...........B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'B..........B............B',
        'BBBBBBBBBBBBBBBBBBBBBBBBB']

    def get_tilemap(self):
        return self._tilemap

    def generate_map(self, cast):
        for y, row in enumerate(self._tilemap):
            for x, column in enumerate(row):

                if column == 'G':
                    enemy_boundary = EnemyBoundary(x, y)
                    cast['enemy_boundaries'].append(enemy_boundary)
                if column == 'B':
                    bush = Bush(x, y)
                    cast['bushes'].append(bush)
                if column == 'P':
                    player  = Player(x, y)
                    cast['player'].append(player)
                if column == 'E':
                    enemy = Enemy(x, y)
                    cast['enemies'].append(enemy)