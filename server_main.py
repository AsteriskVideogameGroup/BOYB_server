from foundations.easy_dependency_injection.FEDContainer import FEDContainer
from foundations.easy_dependency_injection.naiveimplementation.DepthFirstGraphICTranslator import \
    DepthFirstGraphICTranslator
from foundations.easy_dependency_injection.naiveimplementation.JSONSource import JSONSource
from foundations.easy_dependency_injection.naiveimplementation.NaiveLibraryImporter import NaiveLibraryImporter
from foundations.easy_dependency_injection.utils.InjContentTranslator import InjContentTranslator
from foundations.easy_dependency_injection.utils.InjectionSource import InjectionSource

from control.gamemanageusecase.matchmakinghandler import MatchMakingHandler
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

