from foundations.dao.idaoabstractfactory import IDAOAbstractFactory
from foundations.dao.imodedao import IModeDAO
from foundations.dao.iplayerdao import IPlayerDAO
from foundations.dao.pymdm.modedao import ModeDAO
from foundations.dao.pymdm.playerdao import PlayerDAO
from pymodm import connect


class DAOFactory(IDAOAbstractFactory):
    def __init__(self):
        self._modedao: IModeDAO = ModeDAO()
        self._playerdao: IPlayerDAO = PlayerDAO()
        self._uri: str = None

    def init(self):
        print("connessione in corso")
        connect(self._uri)
        print("connesso")

    def getModeDAO(self) -> IModeDAO:
        return self._modedao

    def getPlayerDAO(self) -> IPlayerDAO:
        return self._playerdao

    '''@property
    def modedao(self) -> IModeDAO:
        return self._modedao

    @modedao.setter
    def modedao(self, dao: IModeDAO):
        self._modedao = dao

    @property
    def playerdao(self) -> IPlayerDAO:
        return self._playerdao

    @playerdao.setter
    def playerdao(self, dao: IPlayerDAO):
        self._playerdao = dao'''

    @property
    def uri(self) -> str:
        return self._uri

    @uri.setter
    def uri(self, uri: str):
        self._uri = uri
