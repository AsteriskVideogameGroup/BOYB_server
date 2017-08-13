from typing import List

from foundations.dao.ibobdescriptiondao import IBobDescriptionDAO
from foundations.dao.pymodm.savingadapters.bobdescriptionpersistenceadapter import BobDescriptionPersistenceAdapter
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
            specialpowerid=description.specialpower,
            rangereachable=description.range
        )

        descriptiontosave.save()
        return description

    def getAll(self) -> List[BobDescription]:
        listdescription: List[BobDescription] = list()
        for descriptionpersistent in BobDescriptionPersistenceAdapter.objects.all():
            descriptionpersistent: BobDescriptionPersistenceAdapter
            listdescription.append(descriptionpersistent.get())

        return listdescription
