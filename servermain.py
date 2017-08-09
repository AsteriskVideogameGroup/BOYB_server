from control.gamemanageusecase.matchmakinghandler import MatchMakingHandler
from foundations.dao.idaoabstractfactory import IDAOAbstractFactory
from foundations.geometry.shapedimension import Dimension
from foundations.inversionofcontrol.dicontainer import DepInjContainer
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager
from model.gamemanageusecase.modes.mode import GameMode

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

    # TODO testing
    # inizializzazione database
    daof: IDAOAbstractFactory = container.getObject("daofactory")
    daof.init()

    mapsize: Dimension = Dimension(22, 33)
    newmode: GameMode = GameMode("pepito", mapsize, 4, 300, "ClassicMapElementDisposalStrategy", "ClassicObjectFactory")

    #print(newmode)
    modesave = daof.getModeDAO()

    #modesave.save(newmode)
    mode = modesave.getByID("pepito")
    print(mode)


    #TODO testing


    print(corba.remotize(matchmakinghandler, "matchmakinghandler"))

