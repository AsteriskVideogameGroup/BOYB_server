from foundations.network.clienthandling.client import Client
from foundations.network.corba.icorbamanager import ICorbaManager
from foundations.oophelpers.singleton import SingletonMetaclass


class ClientsRegister(metaclass=SingletonMetaclass):
    def __init__(self):
        self._registeredclients: dict = dict()
        self._corbamanager: ICorbaManager = None

    def init(self, manager: ICorbaManager):
        self._corbamanager = manager

    def get(self, clientid: str) -> Client:

        client: Client = self._registeredclients.get(clientid)

        if client is None:
            client = self._corbamanager.getFromSystem(clientid)
            self._registeredclients[clientid] = client

        return client
