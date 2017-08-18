from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.objects.factories.iobjectrabstractfactory import IObjectAbstractFactory

# factory concrete producibili
from model.gamemanageusecase.objects.factories.classicobjectfactory import ClassicObjectFactory


class ObjectFactoryProvider(metaclass=SingletonMetaclass):
    """"""

    def __init__(self):
        self._factories: dict = dict()

    def getMapObjectFactory(self, factoryid: str) -> IObjectAbstractFactory:

        factory: IObjectAbstractFactory = self._factories.get(factoryid)

        if factory is None:
            strategytoinstantiale = globals()[factoryid]
            factory = strategytoinstantiale()

            if not isinstance(factory, IObjectAbstractFactory):
                raise AttributeError(factoryid + " is not a valid object factory")

            self._factories[factoryid] = factory

        return factory
