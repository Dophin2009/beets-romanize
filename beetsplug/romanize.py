from beets.plugins import BeetsPlugin
from typing import List
import pykakasi


class RomanizePlugin(BeetsPlugin):
    def __init__(self):
        super(RomanizePlugin, self).__init__()
        self.kks = pykakasi.kakasi()
        self.template_funcs['romanize'] = self._romanize

    def _romanize(self, text: str) -> str:
        result = self.kks.convert(text)
        items: List[str] = [item['hepburn'] for item in result]
        return ' '.join(items)
