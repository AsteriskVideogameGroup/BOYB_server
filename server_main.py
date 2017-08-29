from control.gamemanageusecase.matchmakinghandler import MatchMakingHandler
from foundations.persistence.idaoabstractfactory import IDAOAbstractFactory
from foundations.inversionofcontrol.ioccontainer import InversionOfControlContainer
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager

if __name__ == "__main__":

    # inizializzazione container IoC
    container: InversionOfControlContainer = InversionOfControlContainer().init("etc/config.json")

    # inizializzazione comunicazione di rete CORBA
    corbafactory: CorbaManagerFactory = container.getObject("corbamangerfactory")
    corbamanger: ICorbaManager = corbafactory.getCorbaManager()
    corbamanger.init()

    # inizializzazione database
    daofactory: IDAOAbstractFactory = container.getObject("daofactory")
    daofactory.init()

    # inizializzazione ascoltatore di matchaking
    handlername: str = "matchmakinghandler"
    matchmakinghandler: MatchMakingHandler = container.getObject(handlername)
    corbamanger.remotize(matchmakinghandler, handlername)

