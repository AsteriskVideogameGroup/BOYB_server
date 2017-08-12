from control.gamemanageusecase.matchmakinghandler import MatchMakingHandler
from foundations.dao.ibobdescriptiondao import IBobDescriptionDAO
from foundations.dao.idaoabstractfactory import IDAOAbstractFactory
from foundations.dao.imodedao import IModeDAO
from foundations.inversionofcontrol.dicontainer import DepInjContainer
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager

if __name__ == "__main__":

    # inizializzazione container IoC
    container: DepInjContainer = DepInjContainer().init("etc/config.json")

    # inizializzazione comunicazione di rete CORBA
    corbafactory: CorbaManagerFactory = container.getObject("corbamangerfactory")
    corbamanger: ICorbaManager = corbafactory.getCorbaManager()
    corbamanger.init()

    # inizializzazione database
    daofactory: IDAOAbstractFactory = container.getObject("daofactory")
    daofactory.init()

    # TODO test
    #dao: IBobDescriptionDAO = daofactory.getBobDescriptionDAO()
    #print(dao.getAll())
    # TODO test

    # inizializzazione ascoltatore di matchaking
    handlername: str = "matchmakinghandler"
    matchmakinghandler: MatchMakingHandler = container.getObject(handlername)
    corbamanger.remotize(matchmakinghandler, handlername)

