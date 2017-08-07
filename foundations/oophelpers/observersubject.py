import abc


class Subject(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def registerEventListener(self, callback: callable):
        pass

    @abc.abstractmethod
    def detachEventListerners(self, eventid: str):
        pass


