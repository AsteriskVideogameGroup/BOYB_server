from typing import Dict

from foundations.persistence.idaoabstractfactory import IDAOAbstractFactory
from foundations.persistence.iplayerdao import IPlayerDAO
from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.players.player import Player


class PlayerBinder(metaclass=SingletonMetaclass):
    def __init__(self):
        self._daofactory: IDAOAbstractFactory = None
        self._retrievedusers: Dict[str, Player] = dict()

    def getPlayerByID(self, userid: str) -> Player:
        dao: IPlayerDAO = self._daofactory.getPlayerDAO()
        return dao.getByID(userid)

    @property
    def daofactory(self) -> IDAOAbstractFactory:
        return self._daofactory

    @daofactory.setter
    def daofactory(self, factory: IDAOAbstractFactory):
        self._daofactory = factory
