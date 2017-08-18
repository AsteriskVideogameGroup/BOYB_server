from model.gamemanageusecase.objects.classic.classicdestructibleobstacle import ClassicDestructibleObstacle
from model.gamemanageusecase.objects.classic.classicundestructibleobstacle import \
    ClassicUndestructibleObstacle
from model.gamemanageusecase.objects.iobjectrabstractfactory import IObjectAbstractFactory
from model.gamemanageusecase.objects.obstacles.idestructibleobstacle import IDestructibleObstacle
from model.gamemanageusecase.objects.obstacles.iundestructibleobstacle import IUndestructibleObstacle


class ClassicObjectFactory(IObjectAbstractFactory):
    """"""

    def getDestructibleObstacles(self) -> list:
        """"""  # TODO questo deve essere fatto in maniera casuale
        uobstacles: list = list()

        for i in range(0, 4):
            obs: IDestructibleObstacle = ClassicDestructibleObstacle()
            uobstacles.append(obs)

        return uobstacles

    def getUndestructibleOstacles(self) -> list:

        uobstacles: list = list()

        for i in range(0, 4):
            obs: IUndestructibleObstacle = ClassicUndestructibleObstacle()
            uobstacles.append(obs)

        return uobstacles


