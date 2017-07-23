from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.players.player import Player


class PlayerBinder(metaclass=SingletonMetaclass):
    def __init__(self):
        self._retrievedusers: dict = dict()

    def getPlayerByID(self, userid: str):
        """"""  # TODO devi leggere dal database
        return Player(userid)
