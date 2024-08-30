from typing import List
import db.mysql_repo
from model.lex import Lexentry


class Services:

    def __init__(self):
        self.repo = db.mysql_repo.MysqlRepository()

    def load_all(self) -> List[Lexentry]:
        """
        Return all lexical entries from the database
        :return: List[LexEntries]
        """
        return self.repo.load_lexicon()

    def add_entry(self, lexitem: Lexentry) -> bool:
        """
        Add a lexical entry to the database
        :param lexitem:
        :return:
        """
        outcome = self.repo.save_item(lexitem)
        return outcome


if __name__ == "__main__":
    services = Services()
