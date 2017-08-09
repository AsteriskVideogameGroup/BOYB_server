import abc

from model.gamemanageusecase.modes.mode import GameMode


class IModeDAO(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getByID(self, id: str) -> GameMode:
        pass

    @abc.abstractmethod
    def save(self, mode: GameMode) -> GameMode:
        pass

    @abc.abstractmethod
    def update(self, mode: GameMode) -> GameMode:
        pass
