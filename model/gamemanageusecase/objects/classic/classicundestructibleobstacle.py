import math

from foundations.geometry.cartesianposition import Position
from model.gamemanageusecase.objects.obstacles.iundestructibleobstacle import IUndestructibleObstacle


class ClassicUndestructibleObstacle(IUndestructibleObstacle):
    def __init__(self):
        self._position = None

    @property
    def resistence(self) -> int:
        return math.inf  # resistenza infinita

    @property
    def position(self) -> Position:
        return self._position

    @position.setter
    def position(self, newposition: Position):
        self._position = newposition

    def currentPosition(self) -> Position:
        return self.position

    def place(self, newposition: Position):
        self.position = newposition

    def damage(self, damage: int):
        pass  # no op

    def currentResistence(self) -> int:
        return self.resistence
