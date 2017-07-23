from control.gamemanageusecase.gamehandler import GameHandler
from foundations.network.clientbinder import ClientBinder
from foundations.network.client import Client
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager
from model.gamemanageusecase.game.game import Game
from model.gamemanageusecase.modes.mode import GameMode
from model.gamemanageusecase.players.player import Player
from model.gamemanageusecase.players.playerbinder import PlayerBinder
from model.gamemanageusecase.players.room import PlayerRoom


class MatchMaker:
    def __init__(self, mode: GameMode):
        self._unrankedplayerqueue: list = list()  # usiamo un dict per motivi di efficienza
        self._gamemode: GameMode = mode

    def enqueuePlayer(self, client: Client, gameranked: bool):

        if gameranked is False:
            self._unrankedplayerqueue.append(client)
            print("added user: " + str(client.playerid))
            self._makeUnrankedGame()  # tenta di creare una partita
        else:
            pass  # NOTA: non gestiamo in questa iterazione il ranked

    def _makeUnrankedGame(self):

        print("giocatori nella coda: " + str(len(self._unrankedplayerqueue)))

        if len(self._unrankedplayerqueue) >= self._gamemode.numplayers:

            newroom: PlayerRoom = PlayerRoom()

            clientproxies: list = list()

            for i in range(0, self._gamemode.numplayers):
                client: Client = self._unrankedplayerqueue.pop(0)
                player: Player = PlayerBinder().getPlayerByID(client.playerid)
                newroom.join(player)
                clientproxies.append(client)

            newgame: Game = Game(newroom, self._gamemode)

            newgamehandler: GameHandler = GameHandler(newgame, clientproxies)

            # newgamehandler deve essere remoto
            corba: ICorbaManager = CorbaManagerFactory().getCorbaManager()
            corba.remotize(newgamehandler, newgamehandler.gamename)

            # notifica tutti i client
            for clientproxy in clientproxies:
                clientproxy: Client
                clientproxy.notifyGameReady(newgamehandler.gamename)


            print("Game creato\n\n")

            # inizia countdown selezione bob
            newgamehandler.startBobChooseCountdown()
