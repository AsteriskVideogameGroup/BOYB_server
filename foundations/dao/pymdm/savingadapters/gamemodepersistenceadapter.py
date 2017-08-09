from pymodm import MongoModel, fields

from foundations.geometry.shapedimension import Dimension
from model.gamemanageusecase.modes.mode import GameMode


class GameModePersistenceAdapter(MongoModel):

    # attributi da memorizzare
    modename = fields.CharField(primary_key=True)
    mapwidth = fields.IntegerField()
    mapheight = fields.IntegerField()
    gamedurationinseconds = fields.IntegerField()
    mapelementdisposer = fields.CharField()
    maxplayers = fields.IntegerField()
    objectfactoryid = fields.CharField()

    def get(self) -> GameMode:
        dimension: Dimension = Dimension(self.mapwidth, self.mapheight)
        mode: GameMode = GameMode(self.modename, dimension, self.maxplayers,
                                  self.gamedurationinseconds, self.mapelementdisposer,
                                  self.objectfactoryid)

        return mode
