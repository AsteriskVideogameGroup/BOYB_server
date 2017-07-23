from foundations.geometry.shapedimension import Dimension


class GameMode:
    def __init__(self, name: str, mapdimensions: Dimension, maxplayers: int, secgameduration: int,
                 mapelementdisposerid: str, objectfactoryid: str):
        self._modename: str = name
        self._mapdimension: Dimension = mapdimensions
        self._maxplayers: int = maxplayers
        self._gamedurationinseconds: int = secgameduration
        self._mapelementdisposer: str = mapelementdisposerid
        self._objectfactoryid: str = objectfactoryid

    @property
    def name(self) -> str:
        return self._modename

    @property
    def mapdimension(self) -> Dimension:
        return self._mapdimension

    @property
    def mapelementdisposer(self) -> str:
        return self._mapelementdisposer

    @property
    def objectprovider(self) -> str:
        return self._objectfactoryid

    @property
    def numplayers(self):
        return self._maxplayers

    @property
    def duration(self):
        return self._gamedurationinseconds

    def __str__(self) -> str:
        return "MODALITA: \n" + \
               "nome: " + self.name + "\n" + \
               "dimensioni mappa: " + str(self.mapdimension) + "\n" + \
               "numero giocatori: " + str(self.numplayers) + "\n" + \
               "durata in secondi: " + str(self.duration)
