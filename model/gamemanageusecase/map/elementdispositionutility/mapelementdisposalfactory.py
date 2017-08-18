from typing import Dict

from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.map.elementdispositionutility.imapelementdisposalstrategy import \
    IMapElementDisposalStrategy


class MapElementDisposalFactory(metaclass=SingletonMetaclass):
    def __init__(self):
        self._disposalstrategies: dict = dict()

    def getMapElementDisposer(self, strategyid: str) -> IMapElementDisposalStrategy:

        strategy: IMapElementDisposalStrategy = self._disposalstrategies.get(strategyid)

        if strategy is None:
            raise ModuleNotFoundError("Disposal Strategy not found")

        return strategy

    @property
    def strategies(self) -> Dict[str, IMapElementDisposalStrategy]:
        return self._disposalstrategies

    @strategies.setter
    def strategies(self, strategies: Dict[str, IMapElementDisposalStrategy]):
        self._disposalstrategies = strategies
