from cmplex import C

# Napisać testy sprawdzające dodawanie liczb zespolonych
# w załączonym pliku


def test_0():
    x = C(1, 2)
    y = C(2, 3)
    assert C.__add__(x, y) == (3, 5)



