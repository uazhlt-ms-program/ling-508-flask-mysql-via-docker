from app.services import *
from model.lex import Lexentry

raw_in = ('tea', 'tʰi', 'noun', 'dirty bathwater')
lexentry_in = Lexentry(*raw_in)

def test_svc_load_all():
    svc = Services()
    lexicon = svc.load_all()
    assert lexicon is not None
    assert len(lexicon) > 0

def test_svc_add_item():
    svc = Services()
    outcome = svc.add_entry(lexentry_in)
    assert outcome
