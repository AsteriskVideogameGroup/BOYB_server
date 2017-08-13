class BobDescription:
    def __init__(self):
        self._id: str = None
        self._damage: int = 0
        self._contemporaryplaceablebombs: int = 0
        self._basenumlives: int = 1
        self._speed: float = 0
        self._idspecialpower: str = None
        self._range: int = 0

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, newid: str):
        self._id = newid

    @property
    def damage(self) -> int:
        return self._damage

    @damage.setter
    def damage(self, damage: str):
        self._damage = damage

    @property
    def contemporarybombs(self) -> int:
        return self._contemporaryplaceablebombs

    @contemporarybombs.setter
    def contemporarybombs(self, bombs: int):
        self._contemporaryplaceablebombs = bombs

    @property
    def baselives(self) -> int:
        return self._basenumlives

    @baselives.setter
    def baselives(self, lives: int):
        self._basenumlives = lives

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, speed: int):
        self._speed = speed

    @property
    def specialpower(self) -> str:
        return self._idspecialpower

    @specialpower.setter
    def specialpower(self, power: int):
        self._idspecialpower = power

    @property
    def range(self) -> int:
        return self._range
    @range.setter
    def range(self, val: int):
        self._range = val

    def __str__(self):
        return "questa è una descrizione"
