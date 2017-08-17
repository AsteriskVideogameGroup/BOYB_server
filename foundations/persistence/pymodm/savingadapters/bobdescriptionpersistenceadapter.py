from pymodm import MongoModel, fields

from model.gamemanageusecase.characters.bobdescription import BobDescription


class BobDescriptionPersistenceAdapter(MongoModel):
    id = fields.CharField(primary_key=True)
    damage = fields.IntegerField()
    bombs = fields.IntegerField()
    lives = fields.IntegerField()
    speed = fields.FloatField()
    specialpowerid = fields.CharField()
    rangereachable = fields.IntegerField()

    def get(self) -> BobDescription:
        bobdescription: BobDescription = BobDescription()
        bobdescription.id = self.id
        bobdescription.damage = self.damage
        bobdescription.baselives = self.lives
        bobdescription.contemporarybombs = self.bombs
        bobdescription.speed = self.speed
        bobdescription.specialpower = self.specialpowerid
        bobdescription.range = self.rangereachable

        return bobdescription
