from foundations.dao.imodedao import IModeDAO
from foundations.dao.pymdm.savingadapters.gamemodepersistenceadapter import GameModePersistenceAdapter
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
            mapelementdisposer=mode.mapelementdisposer,
            maxplayers=mode.numplayers,
            objectfactoryid=mode.objectprovider
        )

        modetosave.save()
        return mode

    def getByID(self, identifier: str) -> GameMode:
        return GameModePersistenceAdapter.objects.raw({'_id': identifier}).first().get()
