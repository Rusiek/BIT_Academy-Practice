from cmplex import C

# Napisać testy sprawdzające porównywanie liczb zespolonych
# w załączonym pliku

def test_0():
    x = C(3, 1)
    y = C(3, 2)
    assert x.__eq__(y)

def test_1():
    x = C(3, 1)
    y = C(3, 1)
    assert x.__eq__(y)