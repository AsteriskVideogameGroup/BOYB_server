from typing import Callable, Dict

import Pyro4

from foundations.oophelpers.observersubject import Subject
from foundations.sysmessages.gamemessages import GameMessages


@Pyro4.expose
class Client(Subject):
    """# eventi che può lanciare il proxy
    MAPREADYEVENT: str = "mapready"
    GAMEREADYEVENT: str = "gameready\""""

    def notifyGameReady(self, gamehandlerid: str):
        pass

    def notifyMapReady(self):
        pass

    def detachEventListerners(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        pass

    def registerEventListener(self, callback: Callable[[object, GameMessages, Dict[str, any]], None]):
        pass
