from typing import List

from pymodm.queryset import QuerySet

from foundations.persistence.imodedao import IModeDAO
from foundations.persistence.pymodm.savingadapters.gamemodepersistenceadapter import GameModePersistenceAdapter
from model.gamemanageusecase.modes.mode import GameMode


class ModeDAO(IModeDAO):

    def update(self, mode: GameMode) -> GameMode:
        pass

    def save(self, mode: GameMode) -> GameMode:
        modetosave: GameModePersistenceAdapter = GameModePersistenceAdapter(
            modename=mode.name,
            mapwidth=mode.mapdimension.width,
            mapheight=mode.mapdimension.height,
            gamedurationinseconds=mode.duration,
            mapelementdisposer=mode.mapelementdisposerid,
            maxplayers=mode.numplayers,
            objectfactoryid=mode.objectproviderid
        )

        modetosave.save()
        return mode

    def getByID(self, identifier: str) -> GameMode:
        return GameModePersistenceAdapter.objects.raw({'_id': identifier}).first().get()

    def getAll(self) -> List[GameMode]:
        listmodes: List[GameMode] = list()
        for modepersistent in GameModePersistenceAdapter.objects.all():
            modepersistent: GameModePersistenceAdapter
            listmodes.append(modepersistent.get())

        return listmodes


