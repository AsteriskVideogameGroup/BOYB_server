import abc

from model.gamemanageusecase.objects.obstacles.iobstacle import IObstacle


class IDestructibleObstacle(IObstacle, metaclass=abc.ABCMeta):
    pass
