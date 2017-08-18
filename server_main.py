from control.gamemanageusecase.matchmakinghandler import MatchMakingHandler
from foundations.persistence.ibobdescriptiondao import IBobDescriptionDAO
from foundations.persistence.idaoabstractfactory import IDAOAbstractFactory
from foundations.persistence.imodedao import IModeDAO
from foundations.inversionofcontrol.ioccontainer import InversionOfControlContainer
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager
from model.gamemanageusecase.map.elementdispositionutility.imapelementdisposalstrategy import \
    IMapElementDisposalStrategy
from model.gamemanageusecase.map.elementdispositionutility.mapelementdisposalfactory import MapElementDisposalFactory
from model.gamemanageusecase.objects.iobjectrabstractfactory import IObjectAbstractFactory
from model.gamemanageusecase.objects.objectfactoryprovider import ObjectFactoryProvider

if __name__ == "__main__":

    # inizializzazione container IoC
    container: InversionOfControlContainer = InversionOfControlContainer().init("etc/config.json")

    '''# inizializzazione comunicazione di rete CORBA
    corbafactory: CorbaManagerFactory = container.getObject("corbamangerfactory")
    corbamanger: ICorbaManager = corbafactory.getCorbaManager()
    corbamanger.init()

    # inizializzazione database
    daofactory: IDAOAbstractFactory = container.getObject("daofactory")
    daofactory.init()'''

    # TODO test
    oprov: MapElementDisposalFactory = container.getObject("mapdisposalstrategy")
    f: IMapElementDisposalStrategy = oprov.getMapElementDisposer("classic_strategy")
    print(f)
    # TODO test

    '''# inizializzazione ascoltatore di matchaking
    handlername: str = "matchmakinghandler"
    matchmakinghandler: MatchMakingHandler = container.getObject(handlername)
    corbamanger.remotize(matchmakinghandler, handlername)'''
