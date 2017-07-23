from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.game.matchmaker import MatchMaker
from model.gamemanageusecase.modes.mode import GameMode
from model.gamemanageusecase.modes.modebuilder import ModeBuilder


class MatchMakerFactory(metaclass=SingletonMetaclass):
    """"""

    def __init__(self, ):
        self._matchmakers: dict = dict()

    def getMatchMaker(self, modeid: str):
        matchmaker: MatchMaker = self._matchmakers.get(modeid)

        if matchmaker is None:
            mode: GameMode = ModeBuilder().get(modeid)

            matchmaker = MatchMaker(mode)

            self._matchmakers[modeid] = matchmaker

        return matchmaker
