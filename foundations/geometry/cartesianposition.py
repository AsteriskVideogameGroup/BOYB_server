class Position:
    def __init__(self, posx: int, posy: int):
        self._x: int = posx
        self._y: int = posy

    def __eq__(self, other: 'Position'):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other: 'Position'):
        return self == other

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = value
