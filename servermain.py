from control.gamemanageusecase.matchmakinghandler import MatchMakingHandler
from foundations.dependencyinjection.dicontainer import DepInjContainer
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager

if __name__ == "__main__":

    container: DepInjContainer = DepInjContainer().init("etc/config.json")

    factory: CorbaManagerFactory = container.getObject("corbamangerfactory")

    corba: ICorbaManager = factory.getCorbaManager()
    corba.init()

    #ClientsRegister().init(corba)
    #clientregister: ClientsRegister = container.getObject("clientregister")
    #clientregister.init()
    #print(clientregister.corbamanager)

    matchmakinghandler: MatchMakingHandler = container.getObject("matchmakinghandler")

    print(matchmakinghandler.clientsregister)
    print(matchmakinghandler.matchmakingfactory)

    print(corba.remotize(matchmakinghandler, "matchmakinghandler"))

