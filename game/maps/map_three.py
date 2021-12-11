from game.maps.map import Map
from game.sprites.player import Player
from game.sprites.enemy import Enemy
from game.sprites.bush import Bush
from game.sprites.enemy_boundary import EnemyBoundary
from game.sprites.text_sprite import TextSprite
from game.sprites.ground import Ground
from game.sprites.door import Door
from game.sprites.point import Point
from game import constants

class MapThree(Map):
    def __init__(self) -> None:
        super().__init__()
        self._tilemap = [
        'BBBBBBBBBBBDDDBBBBBBBBBBB',
        'B.......................B',
        'B.......................B',
        'BXBBBBBBBBBBBBBBBBBBBB.AB',
        'B.......................X',
        'B.BXBBBBBBBBBBBBBBBBBB..B',
        'B.B........XA....R.....AB',
        'B.B.BXBBBB.BBBBBBBBBBB..B',
        'B.B.B....X.BA......R...AB',
        'B.B.B.RX.B.B.........B..B',
        'B.B.X..B.B.BBBBBBBBBBB..B',
        'B.B.BBXB.B.BA.R........AB',
        'B.X......B.BBBBBBBBBBB..B',
        'B.BBBBBBXB.BA...R......AB',
        'X..........BBBBBBBBBBB..B',
        'BBBBBBBBBBXBAR.........AB',
        'B...G...G...G........B..B',
        'B..GRG.GRG.GRG.......B..B',
        'BBBBXBBBXBBBXBBBBBBBBB.PB',
        '......................BB.']

    def get_tilemap(self):
        return self._tilemap

    def generate_map(self, cast):
        for y, row in enumerate(self._tilemap):
            for x, column in enumerate(row):

                ground = Ground(x, y)
                cast['ground'].append(ground)

                if column == 'P':
                    for player in cast['player']:
                        player.set_position(Point(x * constants.TILESIZE, y * constants.TILESIZE))

                if column == 'R':
                    enemy = Enemy(x, y, 'right')
                    cast['enemies'].append(enemy)

                if column == 'L':
                    enemy = Enemy(x, y, 'left')
                    cast['enemies'].append(enemy)

                if column == 'B':
                    bush = Bush(x, y)
                    cast['bushes'].append(bush)

                if column == 'G':
                    enemy_boundary = EnemyBoundary(x, y, 'clockwise_turn')
                    cast['enemy_boundaries'].append(enemy_boundary)

                if column == 'A':
                    enemy_boundary = EnemyBoundary(x, y, 'full_turn')
                    cast['enemy_boundaries'].append(enemy_boundary)

                if column == 'D':
                    door = Door(x, y)
                    cast['doors'].append(door)

                if column == 'Z':
                    bush = Bush(x, y)
                    enemy_boundary = EnemyBoundary(x, y, 'counterclockwise_turn')
                    cast['bushes'].append(bush)
                    cast['enemy_boundaries'].append(enemy_boundary)

                if column == 'X':
                    bush = Bush(x, y)
                    enemy_boundary = EnemyBoundary(x, y, 'clockwise_turn')
                    cast['bushes'].append(bush)
                    cast['enemy_boundaries'].append(enemy_boundary)    

            self._add_text_sprites(cast)
    
    def _add_text_sprites(self, cast):
        x = 200
        y = 200
        text = '\/ Better hurry up, this goblin is leaving the den'
        text_sprite = TextSprite(x, y, text)
        cast['text_sprites'].append(text_sprite)

        x = 100
        y = 510
        text = 'I guess goblins have parties too...'
        text_sprite = TextSprite(x, y, text)
        cast['text_sprites'].append(text_sprite)