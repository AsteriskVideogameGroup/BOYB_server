from typing import Dict, List

from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.objects.iobjectrabstractfactory import IObjectAbstractFactory

# factory concrete producibili


class ObjectFactoryProvider(metaclass=SingletonMetaclass):
    """"""

    def __init__(self):
        self._factories: Dict[str, IObjectAbstractFactory] = dict()

    def getMapObjectFactory(self, factoryid: str) -> IObjectAbstractFactory:

        factory: IObjectAbstractFactory = self._factories.get(factoryid, None)

        if factory is None:
            raise ModuleNotFoundError("Object Factory not found")

        return factory

    @property
    def factories(self) -> Dict[str, IObjectAbstractFactory]:
        return self._factories

    @factories.setter
    def factories(self, dictfac: Dict[str, IObjectAbstractFactory]):
        self._factories = dictfac
