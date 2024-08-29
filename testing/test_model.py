import pytest
from model.lex import *

test_good = ('coffee', 'ˈkʰɔ.fi', 'noun', 'boiled bean water')
test_bad_form = (3.14, 'ˈkʰɔ.fi', 'noun', 'boiled bean water')
test_bad_prn = ('coffee', 3.14, 'noun', 'boiled bean water')
test_bad_pos = ('coffee', 'ˈkʰɔ.fi', 'NN', 'boiled bean water')
test_bad_def = ('coffee', 'ˈkʰɔ.fi', 'noun', 3.14)


def test_lexentry():
    word = Lexentry(*test_good)
    assert word.written_form == test_good[0]
    assert word.pronunciation == test_good[1]
    assert word.pos == test_good[2]
    assert word.definition == test_good[3]
    with pytest.raises(TypeError):
        word2 = Lexentry(*test_bad_form)
    with pytest.raises(TypeError):
        word2 = Lexentry(*test_bad_prn)
    with pytest.raises(ValueError):
        word2 = Lexentry(*test_bad_pos)
    with pytest.raises(TypeError):
        word2 = Lexentry(*test_bad_def)


def test_equivalence():
    lex1 = Lexentry(*test_good)
    lex2 = Lexentry(*test_good)
    assert lex1 == lex2
