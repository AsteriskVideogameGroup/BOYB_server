import abc

from foundations.persistence.ibobdescriptiondao import IBobDescriptionDAO
from foundations.persistence.imodedao import IModeDAO
from foundations.persistence.iplayerdao import IPlayerDAO


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

    @abc.abstractmethod
    def getBobDescriptionDAO(self) -> IBobDescriptionDAO:
        pass
    # TODO bisogna mettere la gestione dei descrittori dei bob
