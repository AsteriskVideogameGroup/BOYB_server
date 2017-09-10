from exampleobjects.othermodule import MostExample


class ExampleClass(object):

    def __init__(self):
        self._hello: str = None
        self._hamburger: MostExample = None
        self.coccode: object = None

    def print(self):
        print("Testo: " + self._hello)

    @property
    def hello(self) -> str:
        return self._hello

    @hello.setter
    def hello(self, value: str) -> None:
        self._hello = value

    @property
    def hamburger(self) -> MostExample:
        return self._hamburger

    @hamburger.setter
    def hamburger(self, val: MostExample):
        self._hamburger = val


