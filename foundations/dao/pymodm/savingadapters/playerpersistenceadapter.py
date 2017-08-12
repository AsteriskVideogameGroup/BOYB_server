from pymodm import fields, MongoModel

from model.gamemanageusecase.players.player import Player


class PlayerPersistenceAdapter(MongoModel):
    # attributi da memorizzare
    identifier = fields.CharField(primary_key=True)

    def get(self) -> Player:
        return Player(self.identifier)
