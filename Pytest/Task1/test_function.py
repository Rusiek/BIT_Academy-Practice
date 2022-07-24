from function import square
# Napisać cztery testy z dla funckji square dla 0, 1, -1 i 100

def test_x():
    assert square(1) == 1

def test_y():
    assert square(0) == 0

def tesy_z():
    assert square(-1) == 1

def test_p():
    assert square(100) == 10000