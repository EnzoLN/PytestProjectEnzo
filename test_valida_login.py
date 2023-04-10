from valida_login import *
def test_validaUser():
    assert validaUser('a')==False
    assert validaUser('A#')==False
    assert validaUser('A a')==False
    assert validaUser('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')==False
    assert validaUser('A')==True

def test_validaSenha():
    assert validaSenha('Aa!7')==False
    assert validaSenha('Aa7AAAAAAAAAA')==False
    assert validaSenha('Aa!AAAAAAAAAA')==False
    assert validaSenha('a!7aaaaaaaaaaaaaa')==False
    assert validaSenha('A!7AAAAAAAAAAAAAA')==False
    assert validaSenha('A!7aaaaaaaaaaaaaa')==True

def test_validaMsg():
    assert validaMsg('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa') == False
    assert validaMsg('a') == True