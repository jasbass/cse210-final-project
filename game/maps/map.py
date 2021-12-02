class Map:
    def __init__(self) -> None:
        self.tile_map = None

    def generate_map(self, cast):
        raise NotImplementedError("execute not implemented in superclass")