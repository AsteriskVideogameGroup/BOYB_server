import Pyro4

from foundations.network.client import Client
from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.players.player import Player


@Pyro4.behavior(instance_mode="single")
class ClientBinder(metaclass=SingletonMetaclass):
    def __init__(self):
        self._registeredclients: dict = dict()

    @Pyro4.expose
    def registerClient(self, clientproxy: Client):
        self._registeredclients[clientproxy.playerid] = clientproxy
        print(self._registeredclients)

    def getClient(self, player: Player) -> Client:
        return self._registeredclients.get(player.identifier)

    @Pyro4.expose
    @property
    def hello(self):
        return "hello 1!"
