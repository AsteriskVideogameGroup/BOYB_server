from foundations.dao.ibobdescriptiondao import IBobDescriptionDAO
from foundations.dao.idaoabstractfactory import IDAOAbstractFactory
from foundations.dao.imodedao import IModeDAO
from foundations.dao.iplayerdao import IPlayerDAO
from foundations.dao.pymodm.bobdescriptiondao import BobDescriptionDAO
from foundations.dao.pymodm.modedao import ModeDAO
from foundations.dao.pymodm.playerdao import PlayerDAO
from pymodm import connect


class DAOFactory(IDAOAbstractFactory):
    def __init__(self):
        self._modedao: IModeDAO = ModeDAO()
        self._playerdao: IPlayerDAO = PlayerDAO()
        self._bobdescriptiondao: IBobDescriptionDAO = BobDescriptionDAO()
        self._uri: str = None

    def init(self):
        print("connessione in corso")
        connect(self._uri)
        print("connesso")

    def getModeDAO(self) -> IModeDAO:
        return self._modedao

    def getPlayerDAO(self) -> IPlayerDAO:
        return self._playerdao

    def getBobDescriptionDAO(self) -> IBobDescriptionDAO:
        return self._bobdescriptiondao

    @property
    def uri(self) -> str:
        return self._uri

    @uri.setter
    def uri(self, uri: str):
        self._uri = uri
