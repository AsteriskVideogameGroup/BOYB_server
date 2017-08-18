import abc

from model.gamemanageusecase.map.map import Map


class IMapElementDisposalStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def disposeInitialMapState(self, maptosetup: Map):
        pass
