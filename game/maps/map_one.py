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
        'B..GGGGGG...............B',
        'B..GE...G......E........B',
        'B..GGGGGG...............B',
        'B.......................B',
        'B.......................B',
        'B...........P...........B',
        'B.......................B',
        'B.......................B',
        'B.......................B',
        'BBBBBBBBBBBBBBBBBBBBBBBBB']

    def get_tilemap(self):
        return self._tilemap