from typing import List

from control.gamemanageusecase.gamehandler import GameHandler
from foundations.network.clienthandling.client import Client
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager
from model.gamemanageusecase.characters.bobbuilder import BobBuilder
from model.gamemanageusecase.game.game import Game
from model.gamemanageusecase.map.elementdispositionutility.imapelementdisposalstrategy import \
    IMapElementDisposalStrategy
from model.gamemanageusecase.modes.mode import GameMode
from model.gamemanageusecase.players.player import Player
from model.gamemanageusecase.players.playerbinder import PlayerBinder
from model.gamemanageusecase.players.room import PlayerRoom


class MatchMaker:
    def __init__(self, mode: GameMode):
        self._unrankedplayerclientqueue: List[Client] = list()  # usiamo un dict per motivi di efficienza
        self._gamemode: GameMode = mode
        self._corbamanagerfactory: CorbaManagerFactory = None
        self._playerbinder: PlayerBinder = None
        self._bobbuilder: BobBuilder = None

    def enqueuePlayer(self, client: Client, gameranked: bool):

        if gameranked is False:
            self._unrankedplayerclientqueue.append(client)
            print("added user: " + str(client.playerid))
            self._makeUnrankedGame()  # tenta di creare una partita
        else:
            pass  # NOTA: non gestiamo in questa iterazione il ranked

    def _makeUnrankedGame(self):

        print("giocatori nella coda: " + str(len(self._unrankedplayerclientqueue)))

        if len(self._unrankedplayerclientqueue) >= self._gamemode.numplayers:

            newroom: PlayerRoom = PlayerRoom()

            clientproxies: list = list()

            for i in range(0, self._gamemode.numplayers):
                client: Client = self._unrankedplayerclientqueue.pop(0)
                player: Player = self._playerbinder.getPlayerByID(client.playerid)
                newroom.join(player)
                clientproxies.append(client)

            newgame: Game = Game(newroom, self._gamemode)

            newgamehandler: GameHandler = GameHandler(newgame, clientproxies, self._bobbuilder)

            # newgamehandler deve essere remoto
            corba: ICorbaManager = self._corbamanagerfactory.getCorbaManager()
            corba.remotize(newgamehandler, newgamehandler.gamename)

            # notifica tutti i client
            for clientproxy in clientproxies:
                clientproxy: Client
                clientproxy.notifyGameReady(newgamehandler.gamename)


            print("Game creato\n\n")

            # inizia countdown selezione bob
            newgamehandler.startBobChooseCountdown()

    @property
    def corbamanagerfactory(self) -> CorbaManagerFactory:
        return self._corbamanagerfactory

    @corbamanagerfactory.setter
    def corbamanagerfactory(self, manager: CorbaManagerFactory) -> None:
        self._corbamanagerfactory = manager

    @property
    def playerbinder(self) -> PlayerBinder:
        return self._playerbinder

    @playerbinder.setter
    def playerbinder(self, binder: PlayerBinder) -> None:
        self._playerbinder = binder

    @property
    def bobbuilder(self) -> BobBuilder:
        return self._bobbuilder

    @bobbuilder.setter
    def bobbuilder(self, value: BobBuilder) -> None:
        self._bobbuilder = value
