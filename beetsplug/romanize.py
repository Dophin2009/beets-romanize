from beets.plugins import BeetsPlugin
from typing import Optional
from cutlet import Cutlet
import confuse


class RomanizePlugin(BeetsPlugin):
    def __init__(self):
        super(RomanizePlugin, self).__init__()

        try:
            foreign_spelling = self.config['foreign_spelling'].get(bool)
        except confuse.NotFoundError:
            foreign_spelling = False

        self.use_foreign_spelling = foreign_spelling

        self._katsu_hepburn = None
        self._katsu_kunrei = None
        self._katsu_nihon = None

        self.template_funcs['hepburn'] = self._hepburn
        self.template_funcs['kunrei'] = self._kunrei
        self.template_funcs['nihon'] = self._nihon

    def _hepburn(self, text: str) -> str:
        self._katsu_hepburn = self._get_cutlet(self._katsu_hepburn, 'hepburn')
        return self._katsu_hepburn.romaji(text)

    def _kunrei(self, text: str) -> str:
        self._katsu_kunrei = self._get_cutlet(self._katsu_kunrei, 'kunrei')
        return self._katsu_kunrei.romaji(text)

    def _nihon(self, text: str) -> str:
        self._katsu_nihon = self._get_cutlet(self._katsu_nihon, 'nihon')
        return self._katsu_nihon.romaji(text)

    def _get_cutlet(self, katsu: Optional[Cutlet], ty: str):
        if katsu is None:
            katsu = Cutlet(ty)
            katsu.use_foreign_spelling = self.use_foreign_spelling
        return katsu
