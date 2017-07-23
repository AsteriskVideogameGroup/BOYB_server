from foundations.geometry.shapedimension import Dimension
from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.modes.mode import GameMode


class ModeBuilder(metaclass=SingletonMetaclass):
    """"""

    def __init__(self):
        """"""
        self._buildedmodes = {}

    def get(self, modeid: str) -> GameMode:
        mode: GameMode = self._buildedmodes.get(modeid)

        if mode is None:
            mode: GameMode = self._buid(modeid)  # fai build
            self._buildedmodes[modeid] = mode

        return mode

    def _buid(self, modeid: str) -> GameMode:
        ""  # TODO per ora ci accontentiamo di un caricamento solo locale

        mapsize: Dimension = Dimension(4, 6)
        newmode: GameMode = GameMode("aziz", mapsize, 4, 300, "ClassicMapElementDisposalStrategy", "ClassicObjectFactory")
        return newmode
