import Pyro4

from foundations.network.clienthandling.client import Client
from foundations.network.clienthandling.clientregister import ClientsRegister
from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.game.matchmaker import MatchMaker
from model.gamemanageusecase.game.matchmakerfactory import MatchMakerFactory


@Pyro4.behavior(instance_mode="single")
@Pyro4.expose
class MatchMakingHandler(metaclass=SingletonMetaclass):

    def __init__(self):
        self._matchmakingfactory: MatchMakerFactory = None
        self._clientsregister: ClientsRegister = None

    def makeNewGame(self, clientid: str, modeid: str, isranked: bool):
        matchm: MatchMaker = self._matchmakingfactory.getMatchMaker(modeid)  # retrieve del matchmaker di modalità
        client: Client = self._clientsregister.get(clientid)
        matchm.enqueuePlayer(client, isranked)

    @property
    def matchmakingfactory(self) -> MatchMakerFactory:
        return self._matchmakingfactory

    @matchmakingfactory.setter
    def matchmakingfactory(self, factory: MatchMakerFactory) -> None:
        self._matchmakingfactory = factory

    @property
    def clientsregister(self) -> ClientsRegister:
        return self._clientsregister

    @clientsregister.setter
    def clientsregister(self, register: ClientsRegister) -> None:
        self._clientsregister = register



