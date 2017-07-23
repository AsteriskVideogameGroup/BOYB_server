from control.gamemanageusecase.gamehandler import GameHandler
from control.gamemanageusecase.matchmakinghandler import MatchMakingHandler
from foundations.network.clienthandling.client import Client
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager

userid = "user1"


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
    clientproxy: Client = Client("client1", userid)
    corba.remotize(clientproxy, clientproxy.clientid)

    obs: ObserverPartita = ObserverPartita()

    print(clientproxy)

    # clientproxy.gamereadyobserver = obs.gameReady
    # clientproxy.mapreadyobserver = obs.mapReady

    clientproxy.registerEventListener(Client.GAMEREADYEVENT, obs.gameReady)
    clientproxy.registerEventListener(Client.MAPREADYEVENT, obs.mapReady)

    matchmaker: MatchMakingHandler = corba.getFromSystem("matchmakinghandler")

    matchmaker.makeNewGame(clientproxy, "classic", False)
