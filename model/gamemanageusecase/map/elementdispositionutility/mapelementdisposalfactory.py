from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.map.elementdispositionutility.imapelementdisposalstrategy import \
    IMapElementDisposalStrategy

# possibili strategy
from model.gamemanageusecase.map.elementdispositionutility.classicmapelementdisposalstrategy import \
    ClassicMapElementDisposalStrategy


class MapElementDisposalFactory(metaclass=SingletonMetaclass):
    def __init__(self):
        self._disposalstrategies: dict = dict()

    def getMapElementDisposer(self, strategyid: str) -> IMapElementDisposalStrategy:

        strategy: IMapElementDisposalStrategy = self._disposalstrategies.get(strategyid)

        if strategy is None:
            strategytoinstantiale = globals()[strategyid]  # TODO deve essere fatto con IoC
            strategy = strategytoinstantiale()

            if not isinstance(strategy, IMapElementDisposalStrategy):
                raise AttributeError(strategyid + " is not a valid strategy")

            self._disposalstrategies[strategyid] = strategy

        return strategy
