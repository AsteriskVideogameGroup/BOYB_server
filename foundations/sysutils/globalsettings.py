import json

from foundations.oophelpers.singleton import SingletonMetaclass


class GlobalSettings(metaclass=SingletonMetaclass):
    """"""

    def __init__(self, ):
        self._settingpath = "./src/foundation/settings/programsettings.json"
        self._settings = dict()
        self._setup()

    def _setup(self):
        with open(self._settingpath) as settings_file:
            self._settings = {**self._settings, **json.load(settings_file)}

    def setting(self, settingname: str):
        return self._settings.get(settingname)
