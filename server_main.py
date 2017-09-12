from control.gamemanageusecase.matchmakinghandler import MatchMakingHandler
from foundations.ioc.FEDContainer import FEDContainer
from foundations.ioc.naiveimplementation.DepthFirstGraphICTranslator import DepthFirstGraphICTranslator
from foundations.ioc.naiveimplementation.JSONSource import JSONSource
from foundations.ioc.naiveimplementation.NaiveLibraryImporter import NaiveLibraryImporter
from foundations.ioc.utils.InjContentTranslator import InjContentTranslator
from foundations.ioc.utils.InjectionSource import InjectionSource
from foundations.ioc.utils.LibraryInporter import LibraryImporter
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager
from foundations.persistence.idaoabstractfactory import IDAOAbstractFactory

if __name__ == "__main__":

    # configuration source
    source: InjectionSource = JSONSource("etc/config.json")

    # setup libreria ioc
    importer: LibraryImporter = NaiveLibraryImporter()
    trans: InjContentTranslator = DepthFirstGraphICTranslator(importer)
    container: FEDContainer = FEDContainer(trans, source)
    # inizializzazione container IoC
    #container: InversionOfControlContainer = InversionOfControlContainer().init("etc/config.json")

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

