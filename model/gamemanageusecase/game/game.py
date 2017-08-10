import uuid

from model.gamemanageusecase.characters.bob import Bob
from model.gamemanageusecase.map.elementdispositionutility.imapelementdisposal import IMapElementDisposalStrategy
from model.gamemanageusecase.map.elementdispositionutility.mapelementdisposalfactory import MapElementDisposalFactory
from model.gamemanageusecase.map.map import Map
from model.gamemanageusecase.modes.mode import GameMode
from model.gamemanageusecase.objects.factories.iobjectrabstractfactory import IObjectAbstractFactory
from model.gamemanageusecase.objects.objectfactoryprovider import ObjectFactoryProvider
from model.gamemanageusecase.players.room import PlayerRoom


class Game:
    """"""

    def __init__(self, room: PlayerRoom, mode: GameMode):
        """"""
        self._gameid: str = str(uuid.uuid4())
        self._room: PlayerRoom = room
        self._mode: GameMode = mode
        self._map: Map = Map(mode.mapdimension)

    @property
    def players(self) -> PlayerRoom:
        return self._room

    @property
    def mode(self) -> GameMode:
        return self._mode

    @property
    def id(self) -> str:
        return self._gameid

    @property
    def bobs(self) -> list:
        return self._map.bobs

    @property
    def map(self) -> Map:
        return self._map

    def assignBobToPlayer(self, newbob: Bob, playerid: str):
        newbob.owner = self._room.get(playerid)
        self._map.addBob(newbob)

    def prepareGameStart(self):

        # algoritmo di disposizione degli oggetti e bob sulla mappa
        disposer: IMapElementDisposalStrategy = \
            MapElementDisposalFactory().getMapElementDisposer(self.mode.mapelementdisposer)

        # factory per la generazione degli oggetti
        objfactory: IObjectAbstractFactory = ObjectFactoryProvider().getMapObjectFactory(self.mode.objectprovider)

        # aggiunti tutti gli ostacoli alla mappa
        self.map.addDestructibleObstacles(objfactory.getDestructibleObstacles())
        self.map.addUndestructibleObstacles(objfactory.getUndestructibleOstacles())

        # diponi gli ostacoli e bob sulla mappa
        disposer.disposeInitialMapState(self.map)
