from foundations.geometry.shapedimension import Dimension
from model.gamemanageusecase.map.elementdispositionutility.imapelementdisposalstrategy import \
    IMapElementDisposalStrategy
from model.gamemanageusecase.objects.iobjectrabstractfactory import IObjectAbstractFactory


class GameMode:
    def __init__(self, name: str, mapdimensions: Dimension, maxplayers: int, secgameduration: int,
                 mapelementdisposerid: str, objectfactoryid: str):
        self._modename: str = name
        self._mapdimension: Dimension = mapdimensions
        self._maxplayers: int = maxplayers
        self._gamedurationinseconds: int = secgameduration
        self._mapelementdisposerid: str = mapelementdisposerid
        self._objectfactoryid: str = objectfactoryid

        self._objectfactory: IObjectAbstractFactory = None
        self._mapelementdisposer: IMapElementDisposalStrategy = None

    @property
    def name(self) -> str:
        return self._modename

    @property
    def mapdimension(self) -> Dimension:
        return self._mapdimension

    @property
    def mapelementdisposerid(self) -> str:
        return self._mapelementdisposerid

    @property
    def objectproviderid(self) -> str:
        return self._objectfactoryid

    @property
    def numplayers(self):
        return self._maxplayers

    @property
    def duration(self):
        return self._gamedurationinseconds

    @property
    def objectfactory(self):
        return self._objectfactory

    @objectfactory.setter
    def objectfactory(self, value):
        self._objectfactory = value

    @property
    def mapelementdisposer(self):
        return self._mapelementdisposer

    @mapelementdisposer.setter
    def mapelementdisposer(self, value):
        self._mapelementdisposer = value

    def __str__(self) -> str:
        return "MODALITA: \n" + \
               "nome: " + self.name + "\n" + \
               "dimensioni mappa: " + str(self.mapdimension) + "\n" + \
               "numero giocatori: " + str(self.numplayers) + "\n" + \
               "durata in secondi: " + str(self.duration)
