class Map:
    def __init__(self) -> None:
        self.tile_map = None

    def generate_map(self, cast):
        raise NotImplementedError("execute not implemented in superclass")

    def clear_map(self, cast):
        for group in cast:
            if group != 'player':
                cast[group].clear()
        
        assert len(cast['bushes']) == 0