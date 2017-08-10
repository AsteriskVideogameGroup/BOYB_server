from foundations.network.corba.icorbamanager import ICorbaManager
from foundations.network.corba.pyrocorbamanager import PyroCorbaManager
from foundations.oophelpers.singleton import SingletonMetaclass


class CorbaManagerFactory(metaclass=SingletonMetaclass):
    """"""

    def __init__(self):
        self._corbamanager: ICorbaManager = None

    def getCorbaManager(self) -> ICorbaManager:
        return self.corbamanager

    @property
    def corbamanager(self) -> ICorbaManager:
        return self._corbamanager

    @corbamanager.setter
    def corbamanager(self, manager: ICorbaManager) -> None:
        self._corbamanager = manager
        self._corbamanager.init()
