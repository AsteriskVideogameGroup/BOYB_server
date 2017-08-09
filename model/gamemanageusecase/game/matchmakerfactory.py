from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.game.matchmaker import MatchMaker
from model.gamemanageusecase.modes.mode import GameMode
from model.gamemanageusecase.modes.modebuilder import ModeBuilder
from model.gamemanageusecase.players.playerbinder import PlayerBinder


class MatchMakerFactory(metaclass=SingletonMetaclass):
    """"""

    def __init__(self):
        self._matchmakers: dict = dict()
        self._modebuilder: ModeBuilder = None
        self._corbamanagerfactory: CorbaManagerFactory = None
        self._playerbinder: PlayerBinder = None

    def getMatchMaker(self, modeid: str):
        matchmaker: MatchMaker = self._matchmakers.get(modeid)

        if matchmaker is None:
            mode: GameMode = self._modebuilder.get(modeid)

            matchmaker = MatchMaker(mode)
            matchmaker.corbamanagerfactory = self._corbamanagerfactory
            matchmaker.playerbinder = self._playerbinder

            self._matchmakers[modeid] = matchmaker

        return matchmaker

    @property
    def modebuilder(self) -> ModeBuilder:
        return self._modebuilder

    @modebuilder.setter
    def modebuilder(self, value: ModeBuilder) -> None:
        self._modebuilder = value

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
