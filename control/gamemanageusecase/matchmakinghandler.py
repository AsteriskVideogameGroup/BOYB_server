import Pyro4

from foundations.network.clienthandling.client import Client
from foundations.network.clienthandling.clientregister import ClientsRegister
from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.game.matchmaker import MatchMaker
from model.gamemanageusecase.game.matchmakerfactory import MatchMakerFactory


@Pyro4.behavior(instance_mode="single")
@Pyro4.expose
class MatchMakingHandler(metaclass=SingletonMetaclass):

    '''def makeNewGame(self, client: Client, modeid: str, isranked: bool):
        matchm: MatchMaker = MatchMakerFactory().getMatchMaker(modeid)  # retrieve del matchmaker di modalità
        matchm.enqueuePlayer(client, isranked)'''

    def makeNewGame(self, clientid: str, modeid: str, isranked: bool): # TODO deve essere quello buono
        matchm: MatchMaker = MatchMakerFactory().getMatchMaker(modeid)  # retrieve del matchmaker di modalità
        client: Client = ClientsRegister().get(clientid)
        matchm.enqueuePlayer(client, isranked)
