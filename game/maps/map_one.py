from game.maps.map import Map

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