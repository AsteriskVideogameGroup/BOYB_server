from foundations.dao.ibobdescriptiondao import IBobDescriptionDAO
from foundations.dao.pymdm.savingadapters.bobdescriptionpersistenceadapter import BobDescriptionPersistenceAdapter
from model.gamemanageusecase.characters.bobdescription import BobDescription


class BobDescriptionDAO(IBobDescriptionDAO):
    def update(self, description: BobDescription) -> BobDescription:
        pass

    def getByID(self, id: str) -> BobDescription:
        pass

    def save(self, description: BobDescription) -> BobDescription:
        descriptiontosave: BobDescriptionPersistenceAdapter = BobDescriptionPersistenceAdapter(
            id=description.id,
            damage=description.damage,
            bombs=description.contemporarybombs,
            lives=description.baselives,
            speed=description.speed,
            specialpowerid=description.specialpower
        )

        descriptiontosave.save()
        return description
