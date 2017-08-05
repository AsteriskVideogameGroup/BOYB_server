from control.gamemanageusecase.matchmakinghandler import MatchMakingHandler
from foundations.network.clienthandling.clientregister import ClientRegister
from foundations.network.corba.corbamanagerfactory import CorbaManagerFactory
from foundations.network.corba.icorbamanager import ICorbaManager

if __name__ == "__main__":
    corba: ICorbaManager = CorbaManagerFactory().getCorbaManager()

    corba.init()
    ClientRegister().init(corba)

    print(corba.remotize(MatchMakingHandler, "matchmakinghandler"))

