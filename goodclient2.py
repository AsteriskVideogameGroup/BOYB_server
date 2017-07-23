from threading import Thread

from control.gamemanageusecase.gamehandler import GameHandler
from control.gamemanageusecase.matchmakinghandler import MatchMakingHandler
from foundations.geometry.shapedimension import Dimension
from foundations.network.client import Client
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager

'''
def newgame(*args):
    memhandler: MatchMakingHandler = args[0]

if __name__ == "__main__":
    # remotizzazione del proxy client
    corba: ICorbaManager = CorbaManagerFactory().getCorbaManager()
    corba.init()
    clientproxy: ClientProxy = ClientProxy("client2", "user2")
    corba.remotize(clientproxy, clientproxy.id)

    matchmaker: MatchMakingHandler = corba.getFromSystem("matchmakinghandler")

    matchmaker.makeNewGame(clientproxy, "classic", False)
    '''

userid = "user2"


class ObserverPartita:
    def gameReady(self, client: Client):
        '''print("ho ricevuto questo dato: " + gamehandler)

        gamehandler: GameHandler = corba.getFromSystem(gamehandler)

        print(gamehandler)

        gamehandler.chooseBob(userid, "classicbob")'''

        print("il gioco è pronto ")
        print(client.gamehandler)
        # print(client)
        #client.detach(self.gameReady)

        gamehandler: GameHandler = corba.getFromSystem(client.gamehandler)
        gamehandler.chooseBob(userid, "classicbob")

    def mapReady(self, client: Client):
        print("ora so che la mappa è pronta")


if __name__ == "__main__":


    # remotizzazione del proxy client
    corba: ICorbaManager = CorbaManagerFactory().getCorbaManager()
    corba.init()
    clientproxy: Client = Client("client2", userid)
    corba.remotize(clientproxy, clientproxy.clientid)




    obs: ObserverPartita = ObserverPartita()

    # clientproxy.gamereadyobserver = obs.gameReady
    # clientproxy.mapreadyobserver = obs.mapReady

    print(clientproxy)

    clientproxy.registerEventListener(Client.GAMEREADYEVENT, obs.gameReady)
    clientproxy.registerEventListener(Client.MAPREADYEVENT, obs.mapReady)

    matchmaker: MatchMakingHandler = corba.getFromSystem("matchmakinghandler")

    matchmaker.makeNewGame(clientproxy, "classic", False)
