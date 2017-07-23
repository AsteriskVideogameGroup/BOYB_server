class Dimension:
    def __init__(self, width: float, height: float):
        self._width: float = width
        self._height: float = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def __str__(self) -> str:
        return "h: " + str(self.height) + " w: " + str(self.width)



