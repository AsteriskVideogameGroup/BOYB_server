import Pyro4

from foundations.network.clienthandling.client import Client
from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.game.matchmaker import MatchMaker
from model.gamemanageusecase.game.matchmakerfactory import MatchMakerFactory
from foundations.network.clienthandling.clientsregister import ClientsRegister


@Pyro4.behavior(instance_mode="single")
@Pyro4.expose
class MatchMakingHandler(metaclass=SingletonMetaclass):
    def makeNewGame(self, clientid: str, modeid: str, isranked: bool):
        matchm: MatchMaker = MatchMakerFactory().getMatchMaker(modeid)  # retrieve del matchmaker di modalità
        client: Client = ClientsRegister().get(clientid)
        matchm.enqueuePlayer(client, isranked)
