from model.gamemanageusecase.players.player import Player


class PlayerRoom:
    """"""

    def __init__(self):
        self._players: dict = {}

    def join(self, newplayer: Player):
        self._players[newplayer.identifier] = newplayer

    def kick(self, playerid: str) -> Player:
        return self._players.pop(playerid)

    @property
    def lenght(self):
        return len(self._players)

    @property
    def lstplayers(self):
        return self._players

    def get(self, playerid: str) -> Player:
        return self._players.get(playerid)


