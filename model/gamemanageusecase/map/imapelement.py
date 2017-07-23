import abc

from foundations.geometry.cartesianposition import Position


class IMapElement(metaclass=abc.ABCMeta):
    """"""

    @abc.abstractmethod
    def currentPosition(self) -> Position:
        pass

    @abc.abstractmethod
    def place(self, newposition: Position):
        pass
