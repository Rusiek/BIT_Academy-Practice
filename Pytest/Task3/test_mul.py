from cmplex import C

# Napisać testy sprawdzające mnożenie liczb zespolonych
# w załączonym pliku

def test_0():
    x = C(3, 1)
    y = C(3, 2)
    assert x.__mul__(y) == C(7, 9)

def test_1():
    x = C(3, 1)
    y = C(3, 2)
    assert x.__mul__(y) == C(7, 6)