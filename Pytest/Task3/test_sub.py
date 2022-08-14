from random import randint
from cmplex import C

# Napisać testy sprawdzające odejmowanie liczb zespolonych
# w załączonym pliku
def test_A():
    assert C(0, 0) - C(0, 0) == C(0, 0)

def test_B():
    assert C(0, -5) - C(-2, 0) == C(2, -5)

def test_C():
    for i in range(10):
        tab = [randint(-100, 100) for i in range(4)]
        assert C(tab[0], tab[1]) - C(tab[2], tab[3]) == C(tab[0] - tab[2], tab[1] - tab[3])