from beets.plugins import BeetsPlugin
from typing import List
from cutlet import Cutlet


class RomanizePlugin(BeetsPlugin):
    def __init__(self):
        super(RomanizePlugin, self).__init__()
        self._katsu = Cutlet()
        self.template_funcs['romanize'] = self._romanize

    def _romanize(self, text: str) -> str:
        return self._katsu.slug(text)
