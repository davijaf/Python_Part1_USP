from vogais import vogal

def test_vogaisa():
    assert vogal("a") == True

def test_vogaise():
    assert vogal("e") == True

def test_vogaisi():
    assert vogal("i") == True

def test_vogaiso():
    assert vogal("o") == True

def test_vogaisu():
    assert vogal("u") == True

def test_vogaisa2():
    assert vogal("A") == True

def test_vogaise2():
    assert vogal("E") == True

def test_vogaisi2():
    assert vogal("I") == True

def test_vogaiso2():
    assert vogal("O") == True

def test_vogaisu2():
    assert vogal("U") == True

def test_vogais0():
    assert vogal(0) == False

def test_vogaisb():
    assert vogal("b") == False

def test_vogaisz():
    assert vogal("z") == False
