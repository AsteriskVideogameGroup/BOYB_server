import time
import uuid
from threading import Thread

import Pyro4

from foundations.network.clienthandling.client import Client
from model.gamemanageusecase.characters.bob import Bob
from model.gamemanageusecase.characters.bobbuilder import BobBuilder
from model.gamemanageusecase.game.game import Game
from model.gamemanageusecase.players.player import Player


class GameHandler:

    _CHOOSETIME: int = 20

    def __init__(self, newgame: Game, clientproxies: list, bobbuilder: BobBuilder):
        self._uniquename = str(uuid.uuid4())
        self._currentgame: Game = newgame
        self._mapready: bool = False
        self._clients: list = clientproxies
        self._bobbuilder: BobBuilder = bobbuilder

    @property
    def gamename(self) -> str:
        return self._uniquename

    def startBobChooseCountdown(self):
        Thread(target=self._bobSelectionDaemon, args=()).start()

    @Pyro4.expose
    def chooseBob(self, playerid: str, bobid: str = "random"):
        newbob: Bob = self._bobbuilder.build(bobid)
        self._currentgame.assignBobToPlayer(newbob, playerid)
        print("Ho assegnato bob {0} al player {1}".format(bobid, playerid))

    def _bobSelectionDaemon(self):

        steptime: float = 0.1
        aweitedtime: float = 0

        numplayers: int = self._currentgame.players.numplayers

        loopcondition: bool = True
        someonehasntabob: bool = True

        while loopcondition:
            time.sleep(steptime)
            aweitedtime += steptime
            someonehasntabob = (len(self._currentgame.bobs) < numplayers)
            loopcondition = someonehasntabob and aweitedtime <= GameHandler._CHOOSETIME

        if someonehasntabob:  # se qualche giocatore non ha ancora un bob
            bobowners: list = list()  # lista dei player che hanno un bob

            for bob in self._currentgame.bobs:
                bob: Bob
                bobowners.append(bob.owner)

            for player in bobowners:
                player: Player
                if player not in self._currentgame.players.lstplayers:
                    self.chooseBob(player.identifier)

        self._prepareGame()  # si può ora preparare la mappa per l'avvio del Game

    def _prepareGame(self):

        # imponi al game di effettuare l'inizializzazione
        self._currentgame.prepareGameStart()

        print("prepare game effettuato")

        # notifica tutti i player
        for client in self._clients:
            client: Client
            client.notifyMapReady()
