from foundations.dao.iplayerdao import IPlayerDAO
from model.gamemanageusecase.players.player import Player


class PlayerDAO(IPlayerDAO):

    def save(self, player: Player) -> Player:
        pass

    def update(self, player: Player) -> Player:
        pass

    def getByID(self, id: str) -> Player:
        pass