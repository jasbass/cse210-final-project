from game.maps.map import Map
from game.sprites.player import Player
from game.sprites.enemy import Enemy
from game.sprites.bush import Bush
from game.sprites.enemy_boundary import EnemyBoundary
from game.sprites.ground import Ground
from game.sprites.point import Point
from game.sprites.door import Door
from game.sprites.text_sprite import TextSprite
from game import constants

class MapOne(Map):
    def __init__(self) -> None:
        super().__init__()
        self._tilemap = [
        'BBBBBBBBBBBDDDBBBBBBBBBBB',
        'B.........B...B.........B',
        'Q.......RAB...B.........B',
        'B.........B...B.........B',
        'B.............B.........B',
        'B....B........BAR.......Q',
        'B.......................B',
        'B..................B....B',
        'Q.......RA..............B',
        'B.......................B',
        'B.......................B',
        'B..............AR.......Q',
        'B....B.B................B',
        'B.......................B',
        'Q.......RA..............B',
        'B.......................B',
        'B..............AR.......Q',
        'B.......................B',
        'BBBBBBBBBBB.P.BBBBBBBBBBB',
        '...........BBB...........']

    def get_tilemap(self):
        return self._tilemap

    def generate_map(self, cast):
        for y, row in enumerate(self._tilemap):
            for x, column in enumerate(row):

                ground = Ground(x, y)
                cast['ground'].append(ground)

                if column == 'A':
                    enemy_boundary = EnemyBoundary(x, y, 'full_turn')
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
                    
                if column == 'Q':
                    bush = Bush(x, y)
                    enemy_boundary = EnemyBoundary(x, y, 'full_turn')
                    cast['bushes'].append(bush)
                    cast['enemy_boundaries'].append(enemy_boundary)

        self._add_text_sprites(cast)
    
    def _add_text_sprites(self, cast):
        x = 200
        y = 200
        text = 'How did you get here! This must be a goblin camp! \n Quick, run while they aren\'t looking!! (wasd)'
        text_sprite = TextSprite(x, y, text)
        cast['text_sprites'].append(text_sprite)
        