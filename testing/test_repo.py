from db.mysql_repo import MysqlRepository
from model.lex import Lexentry

raw_out = [('coffee', 'ˈkʰɔ.fi', 'noun', 'boiled bean water'),
           ('drink', 'dɹɪŋk', 'verb', 'to imbibe')]

lexentries_out = [Lexentry(*item) for item in raw_out]


def test_load_dict():
    repo = MysqlRepository()
    result = repo.load_lexicon()
    foundmatch = [any([item == entry for entry in lexentries_out]) for item in result]
    assert all(foundmatch)
