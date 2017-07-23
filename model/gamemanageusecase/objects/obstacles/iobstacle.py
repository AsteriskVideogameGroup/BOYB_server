import abc

from model.gamemanageusecase.map.imapelement import IMapElement


class IObstacle(IMapElement, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def damage(self, damage: int):
        pass

    @abc.abstractmethod
    def currentResistence(self) -> int:
        pass
