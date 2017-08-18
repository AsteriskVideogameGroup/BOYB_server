import copy

from foundations.geometry.cartesianposition import Position
from model.gamemanageusecase.objects.obstacles.idestructibleobstacle import IDestructibleObstacle


class ClassicDestructibleObstacle(IDestructibleObstacle):
    def __init__(self):
        self._position: Position = None
        self._health: int = 3

    def currentPosition(self) -> Position:
        return copy.deepcopy(self._position)

    def place(self, newposition: Position):
        self._position = newposition

    def damage(self, damage: int):
        self._health -= damage

    def currentResistence(self) -> int:
        return self._health
