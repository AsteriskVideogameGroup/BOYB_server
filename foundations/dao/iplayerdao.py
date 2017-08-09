import abc

from model.gamemanageusecase.players.player import Player


class IPlayerDAO(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getByID(self, id: str) -> Player:
        pass

    @abc.abstractmethod
    def save(self, player: Player) -> Player:
        pass

    @abc.abstractmethod
    def update(self, player: Player) -> Player:
        pass
