from typing import Dict

from foundations.easy_dependency_injection.utils.InjContentTranslator import InjContentTranslator
from foundations.easy_dependency_injection.utils.InjectionSource import InjectionSource


class FEDContainer:
    def __init__(self, translator: InjContentTranslator, source: InjectionSource):
        self._objectTranslator: InjContentTranslator = translator
        self._source: InjectionSource = source
        self._translatedObjects: Dict[str, object] = dict()

    def getObject(self, objectid: str) -> object:

        requested = self._translatedObjects.get(objectid)

        if requested is None:
            requested = self._objectTranslator.translate(self._source, objectid, self._translatedObjects)

        return requested




