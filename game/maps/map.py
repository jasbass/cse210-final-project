class Map:
    def __init__(self) -> None:
        self.tile_map = None

    def draw_tilemap(self):
        raise NotImplementedError("execute not implemented in superclass")