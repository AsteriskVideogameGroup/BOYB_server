import Pyro4

from foundations.geometry.shapedimension import Dimension
from foundations.network.client import Client
from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.game.matchmaker import MatchMaker
from model.gamemanageusecase.game.matchmakerfactory import MatchMakerFactory


@Pyro4.behavior(instance_mode="single")
@Pyro4.expose
class MatchMakingHandler(metaclass=SingletonMetaclass):
    def makeNewGame(self, client: Client, modeid: str, isranked: bool):
        matchm: MatchMaker = MatchMakerFactory().getMatchMaker(modeid)  # retrieve del matchmaker di modalità
        matchm.enqueuePlayer(client, isranked)
