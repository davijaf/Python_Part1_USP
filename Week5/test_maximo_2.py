from maximo_2 import maximo

def test_maximo0():
    assert maximo(0,1) == 1

def test_maximo1():
    assert maximo(1,2) == 2

def test_maximo2():
    assert maximo(3,2) == 3

def test_maximo3():
    assert maximo(1,0) == 1

def test_maximo4():
    assert maximo(0,0) == 0

def test_maximo4():
    assert maximo(0,-1) == 0