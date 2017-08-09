import abc

from foundations.dao.imodedao import IModeDAO
from foundations.dao.iplayerdao import IPlayerDAO


class IDAOAbstractFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def init(self):
        pass

    @abc.abstractmethod
    def getPlayerDAO(self) -> IPlayerDAO:
        pass

    @abc.abstractmethod
    def getModeDAO(self) -> IModeDAO:
        pass
