import copy
from typing import List

from foundations.geometry.shapedimension import Dimension
from model.gamemanageusecase.characters.bob import Bob
from model.gamemanageusecase.objects.obstacles.iobstacle import IObstacle


class Map:
    """"""

    def __init__(self, dimensions: Dimension):
        self._bobplaced: dict = dict()
        self._destructibleobstacles: list = list()
        self._undestructibleobstacles: list = list()
        self._dimensions = dimensions

    @property
    def bobs(self) -> list:
        return list(self._bobplaced.values())

    @property
    def dimensions(self):
        return copy.deepcopy(self._dimensions)

    @property
    def numbobs(self) -> int:
        return len(self._bobplaced)

    @property
    def destructibiles(self) -> list:
        return self._destructibleobstacles

    @destructibiles.setter
    def destructibiles(self, obstacles: list):
        self._destructibleobstacles = obstacles

    @property
    def undescructibles(self) -> list:
        return self._undestructibleobstacles

    @undescructibles.setter
    def undescructibles(self, obstacles: list):
        self._undestructibleobstacles = obstacles

    @property
    def occupiedpositions(self) -> list:
        occupiedpos: list = list()

        for bob in self.bobs:
            bob: Bob  # annotazione di tipo
            print(bob.currentPosition())
            occupiedpos.append(bob.position)

        for obstacle in self.undescructibles:
            obstacle: IObstacle
            print(obstacle.currentPosition())
            occupiedpos.append(obstacle.currentPosition())

        for obstacle in self.destructibiles:
            obstacle: IObstacle
            print(obstacle.currentPosition())
            occupiedpos.append(obstacle.currentPosition())

        return occupiedpos

    def addBob(self, newcome: Bob):
        self._bobplaced[newcome.id] = newcome

    def removeBob(self, bobid: str) -> Bob:
        return self._bobplaced.pop(bobid)

    def addUndestructibleObstacle(self, obstacle: IObstacle):
        self._undestructibleobstacles.append(obstacle)

    def addDestructibleObstacle(self, obstacle: IObstacle):
        self._destructibleobstacles.append(obstacle)

    def addUndestructibleObstacles(self, lstundestructibles: list):

        for mapobject in lstundestructibles:
            self._undestructibleobstacles.append(mapobject)

    def addDestructibleObstacles(self, lstundestructibles: list):

        for mapobject in lstundestructibles:
            self._destructibleobstacles.append(mapobject)


