from foundations.persistence.idaoabstractfactory import IDAOAbstractFactory
from foundations.persistence.imodedao import IModeDAO
from foundations.geometry.shapedimension import Dimension
from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.map.elementdispositionutility.mapelementdisposalfactory import MapElementDisposalFactory
from model.gamemanageusecase.modes.mode import GameMode
from model.gamemanageusecase.objects.objectfactoryprovider import ObjectFactoryProvider


class ModeBuilder(metaclass=SingletonMetaclass):
    """"""

    def __init__(self):
        """"""
        self._buildedmodes = {}
        self._daofactory: IDAOAbstractFactory = None
        self._disposerfactory: MapElementDisposalFactory = None
        self._objectfactoryprovider: ObjectFactoryProvider = None

    def get(self, modeid: str) -> GameMode:
        print("cerco la mode")
        mode: GameMode = self._buildedmodes.get(modeid)

        if mode is None:
            mode: GameMode = self._buid(modeid)  # fai build
            self._buildedmodes[modeid] = mode

        return mode

    def _buid(self, modeid: str) -> GameMode:
        modesave: IModeDAO = self._daofactory.getModeDAO()

        retrievedmode: GameMode = modesave.getByID(modeid)
        retrievedmode.objectfactory = self._objectfactoryprovider.getMapObjectFactory(retrievedmode.objectproviderid)
        retrievedmode.mapelementdisposer = self._disposerfactory.getMapElementDisposer(retrievedmode.mapelementdisposerid)

        return retrievedmode

    @property
    def daofactory(self) -> IDAOAbstractFactory:
        return self._daofactory

    @daofactory.setter
    def daofactory(self, factory: IDAOAbstractFactory):
        self._daofactory = factory

    @property
    def elementdisposerfactory(self):
        return self._disposerfactory

    @elementdisposerfactory.setter
    def elementdisposerfactory(self, value):
        self._disposerfactory = value

    @property
    def objectfactoryprovider(self):
        return self._objectfactoryprovider

    @objectfactoryprovider.setter
    def objectfactoryprovider(self, value):
        self._objectfactoryprovider = value
