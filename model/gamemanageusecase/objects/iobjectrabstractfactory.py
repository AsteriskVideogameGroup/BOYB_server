import abc


class IObjectAbstractFactory(metaclass=abc.ABCMeta):
    """"""

    @abc.abstractmethod
    def getDestructibleObstacles(self) -> list:
        """
        Getter for the destructible obstacles for a given mode

        :return: a list of differents destructible obstacles
        """
        pass

    @abc.abstractmethod
    def getUndestructibleOstacles(self) -> list:
        """
        Getter for the destructible obstacles for a given mode

        :return: a list of differents destructible obstacles
        """
        pass
