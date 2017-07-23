class Player:
    def __init__(self, uniqueid: str):
        """"""
        self._uniqueid = uniqueid

    @property
    def identifier(self):
        return self._uniqueid

    def __str__(self):
        return "Player ID: " + self.identifier
