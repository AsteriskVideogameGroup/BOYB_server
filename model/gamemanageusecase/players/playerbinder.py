from typing import Dict

from foundations.dao.idaoabstractfactory import IDAOAbstractFactory
from foundations.dao.iplayerdao import IPlayerDAO
from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.players.player import Player


class PlayerBinder(metaclass=SingletonMetaclass):
    def __init__(self):
        self._daofactory: IDAOAbstractFactory = None
        self._retrievedusers: Dict[str, Player] = dict()

    def getPlayerByID(self, userid: str) -> Player:
        """"""  # TODO devi leggere dal database
        dao: IPlayerDAO = self._daofactory.getPlayerDAO()
        # TODO implementare DAO
        # player: Player = dao.getByID(userid)
        # return dao.getByID("pepito")  # TODO rimuovere
        return Player(userid)

    @property
    def daofactory(self) -> IDAOAbstractFactory:
        return self._daofactory

    @daofactory.setter
    def daofactory(self, factory: IDAOAbstractFactory):
        self._daofactory = factory
