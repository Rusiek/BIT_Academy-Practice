from cmplex import C

# Napisać testy sprawdzające dodawanie liczb zespolonych
# w załączonym pliku


def test_0():
    x = C(1, 2)
    y = C(2, 3)
    assert x.__add__(y) == C(3, 5)

def test_1():
    x = C(1, 2)
    y = C(2, 3)
    assert x.__add__(y) == C(3, 3)



