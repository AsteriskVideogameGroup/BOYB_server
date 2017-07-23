import copy
import uuid

from foundations.geometry.cartesianposition import Position
from model.gamemanageusecase.characters.bobdescription import BobDescription
from model.gamemanageusecase.map.imapelement import IMapElement
from model.gamemanageusecase.players.player import Player


class Bob(IMapElement):
    def __init__(self, description: BobDescription):
        self._bobdescription: BobDescription = description
        self._player: Player = None
        self._currentposition: Position = None
        self._uniquetemporaryid: str = str(uuid.uuid4())  # id univoco per il bob nella partita

    @property
    def owner(self) -> Player:
        return self._player

    @owner.setter
    def owner(self, owner: Player):
        self._player = owner

    @property
    def position(self) -> Position:
        return copy.deepcopy(self._currentposition)

    @position.setter
    def position(self, newposition: Position):
        self._currentposition = newposition

    @property
    def id(self) -> str:
        return self._uniquetemporaryid

    def currentPosition(self) -> Position:
        return self.position

    def place(self, newposition: Position):
        self._currentposition = newposition

    def __str__(self):
        return "Bob\n" + \
               "Descrizione: " + self._bobdescription.__str__() + "\n" + \
               "Proprietario: " + self.owner.__str__() + "\n" + \
               "ID: " + self.id
