import abc

from model.gamemanageusecase.objects.obstacles.iobstacle import IObstacle


class IUndestructibleObstacle(IObstacle, metaclass=abc.ABCMeta):
    pass
