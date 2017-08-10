from foundations.oophelpers.singleton import SingletonMetaclass
from model.gamemanageusecase.characters.bobdescription import BobDescription


class BobCatalog(metaclass=SingletonMetaclass):  # bob description factory
    """"""

    def __init__(self):
        """"""
        self._descriptions = {}

    def getDescription(self, descriptionid: str) -> BobDescription:

        bobdescription: BobDescription = self._descriptions.get(descriptionid)

        if bobdescription is None:
            bobdescription = BobDescription()
            """""" # TODO questi dati devono essere presi da un DB"""
            self._descriptions[descriptionid] = bobdescription

        return bobdescription


