import abc
from model.lex import *
from typing import List


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_lexicon(self) -> List[Lexentry]:
        """
        load all lexical items in the repository
        :return: a list of Lexentry items
        """
        raise NotImplementedError

    @abc.abstractmethod
    def save_item(self, lex_item: Lexentry) -> bool:
        """
        store a lexical item in the repository
        :return: True if successful, False if not
        """
        raise NotImplementedError
