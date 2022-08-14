from random import randint
from cmplex import C

# Napisać testy sprawdzające mnożenie liczb zespolonych
# w załączonym pliku
def test_A():
    assert C(0, 0) * C(0, 0) == C(0, 0)

def test_B():
    assert C(2, 1) * C(5, -1) == C(11, 3)

def test_C():
    for i in range(5):
        tab = [randint(-100, 100) for i in range(4)]
        assert C(tab[0], tab[1]) * C(tab[2], tab[3]) == C((tab[0] * tab[2] - tab[1] * tab[3]), (tab[0] * tab[3] + tab[1] * tab[2]))