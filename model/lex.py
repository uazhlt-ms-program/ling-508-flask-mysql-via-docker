from enum import Enum


class POS(Enum):

    NOUN = 'noun'
    VERB = 'verb'
    ADV = 'adv'
    ADJ = 'adj'
    ADP = 'adp'
    DET = 'det'


class Lexentry:

    def __init__(self, written_form, pronunciation, pos, definition):
        self.written_form = written_form
        self.pronunciation = pronunciation
        self.pos = pos
        self.definition = definition

    @property
    def written_form(self):
        return self._written_form

    @written_form.setter
    def written_form(self, wf):
        if not isinstance(wf, str):
            raise TypeError(f"Written form must be a string; was {type(wf)}")
        self._written_form = wf

    @property
    def pronunciation(self):
        return self._pronunciation

    @pronunciation.setter
    def pronunciation(self, pr):
        if not isinstance(pr, str):
            raise TypeError(f"Pronunciation must be a string; was {type(pr)}")
        self._pronunciation = pr

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        if not isinstance(pos, str):
            raise TypeError(f"POS must be a string; was {type(pos)}")
        if pos not in {tag.value for tag in POS}:
            raise ValueError(f"POS must be from controlled vocab; was {pos}")
        self._pos = pos

    @property
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, defn):
        if not isinstance(defn, str):
            raise TypeError(f"Definition must be a string; was {type(defn)}")
        self._definition = defn

    def __eq__(self, other):
        attributes = [a for a in dir(self) if not a.startswith('__')
                      and not callable(getattr(self, a))]
        comparison = [getattr(self, attrib) == getattr(other, attrib) for attrib in attributes]
        return all(comparison)
