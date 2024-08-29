import abc
from model.lex import *
from typing import List


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_lexicon(self) -> List[Lexentry]:
        raise NotImplementedError
