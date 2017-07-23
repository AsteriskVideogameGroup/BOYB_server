from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.map.elementdispositionutility.imapelementdisposal import IMapElementDisposalStrategy

# possibili strategy
from model.gamemanageusecase.map.elementdispositionutility.classicmapelementdisposalstrategy import \
    ClassicMapElementDisposalStrategy


class MapElementDisposalFactory(metaclass=SingletonMetaclass):

    def __init__(self):
        self._builtstrategies: dict = dict()

    def getMapElementDisposer(self, strategyid: str) -> IMapElementDisposalStrategy:

        strategy: IMapElementDisposalStrategy = self._builtstrategies.get(strategyid)

        if strategy is None:
            strategytoinstantiale = globals()[strategyid]
            strategy = strategytoinstantiale()

            if not isinstance(strategy, IMapElementDisposalStrategy):
                raise AttributeError(strategyid + " is not a valid strategy")

            self._builtstrategies[strategyid] = strategy


        return strategy
