from control.gamemanageusecase.matchmakinghandler import MatchMakingHandler
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager

if __name__ == "__main__":
    corba: ICorbaManager = CorbaManagerFactory().getCorbaManager()
    corba.init()
    corba.remotize(MatchMakingHandler, "matchmakinghandler")

