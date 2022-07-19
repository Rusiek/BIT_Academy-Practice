from cmplex import C

# Napisać testy sprawdzające odejmowanie liczb zespolonych
# w załączonym pliku

def test_0():
    x = C(1, 2)
    y = C(2, 3)
    assert x.__sub__(y) == C(-1, -1)

def test_1():
    x = C(1, 2)
    y = C(2, 3)
    assert x.__sub__(y) == C(0, -1)