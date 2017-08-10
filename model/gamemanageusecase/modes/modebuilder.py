from foundations.dao.idaoabstractfactory import IDAOAbstractFactory
from foundations.dao.imodedao import IModeDAO
from foundations.geometry.shapedimension import Dimension
from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.modes.mode import GameMode


class ModeBuilder(metaclass=SingletonMetaclass):
    """"""

    def __init__(self):
        """"""
        self._buildedmodes = {}
        self._daofactory: IDAOAbstractFactory = None

    def get(self, modeid: str) -> GameMode:
        print("cerco la mode")
        mode: GameMode = self._buildedmodes.get(modeid)

        if mode is None:
            mode: GameMode = self._buid(modeid)  # fai build
            self._buildedmodes[modeid] = mode

        return mode

    def _buid(self, modeid: str) -> GameMode:
        modesave: IModeDAO = self._daofactory.getModeDAO()
        return modesave.getByID(modeid)

    @property
    def daofactory(self) -> IDAOAbstractFactory:
        return self._daofactory

    @daofactory.setter
    def daofactory(self, factory: IDAOAbstractFactory):
        self._daofactory = factory
