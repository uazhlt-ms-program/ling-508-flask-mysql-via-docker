from db.mysql_repo import MysqlRepository
from model.lex import Lexentry

raw_out = [('coffee', 'ˈkʰɔ.fi', 'noun', 'boiled bean water'),
           ('drink', 'dɹɪŋk', 'verb', 'to imbibe')]
raw_in = ('tea', 'tʰi', 'noun', 'dirty bathwater')

lexentries_out = [Lexentry(*item) for item in raw_out]
lexentry_in = Lexentry(*raw_in)


def test_load_dict():
    repo = MysqlRepository()
    result = repo.load_lexicon()
    foundmatch = [any([item == entry for entry in lexentries_out]) for item in result]
    assert all(foundmatch)

def test_save_item():
    repo = MysqlRepository()
    length_before = len(repo.load_lexicon())
    outcome = repo.save_item(lexentry_in)
    assert outcome
    length_after = len(repo.load_lexicon())
    assert length_after == length_before + 1
