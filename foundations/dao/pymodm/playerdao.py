from foundations.dao.iplayerdao import IPlayerDAO
from foundations.dao.pymodm.savingadapters.playerpersistenceadapter import PlayerPersistenceAdapter
from model.gamemanageusecase.players.player import Player


class PlayerDAO(IPlayerDAO):

    def save(self, player: Player) -> Player:
        playertosave: PlayerPersistenceAdapter = PlayerPersistenceAdapter(
            identifier=player.identifier
        )

        playertosave.save()
        return player

    def update(self, player: Player) -> Player:
        pass

    def getByID(self, identifier: str) -> Player:
        return PlayerPersistenceAdapter.objects.raw({'_id': identifier}).first().get()