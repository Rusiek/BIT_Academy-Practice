from cmplex import C
from random import randint

# Napisać testy sprawdzające porównywanie liczb zespolonych
# w załączonym pliku

def test():
    for _ in range(100):
        x1 = randint(-10 ** 10, 10 ** 10)
        x2 = randint(-10 ** 10, 10 ** 10)
        y1 = randint(-10 ** 10, 10 ** 10)
        y2 = randint(-10 ** 10, 10 ** 10)
        assert (C(x1, y1) == C(x2, y2)) is (x1 == x2 and y1 == y2)