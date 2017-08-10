from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.characters.bob import Bob
from model.gamemanageusecase.characters.bobcatalog import BobCatalog, BobDescription


class BobBuilder(metaclass=SingletonMetaclass):
    def __init__(self):
        self._bobcatalog: BobCatalog = BobCatalog()

    def build(self, bobid: str = "random"):
        bobdescription: BobDescription = self._bobcatalog.getDescription(bobid)
        return Bob(bobdescription)
