from cmplex import C
from random import randint
# Napisać testy sprawdzające porównywanie liczb zespolonych
# w załączonym pliku


class TestCmp:
    def test_A(self):
        x1 = randint(0, 10**10)
        y1 = randint(0, 10**10)

        C1 = C(x1, y1)
        C2 = C(x1, y1)
        assert (C1 == C2) == (C1.x == C2.x and C1.y == C2.y)

    def test_B(self):
        x1 = randint(10**10, 10**20)
        x2 = randint(10**10, 10**20)

        y1 = randint(10**10, 10**20)
        y2 = randint(10**10, 10**20)

        C1 = C(x1, y1)
        C2 = C(x2, y2)
        assert (C1 == C2) == (C1.x == C2.x and C1.y == C2.y)

    def test_C(self):
        x1 = randint(-10**30, 10**10)
        x2 = randint(-10**30, 10**10)

        y1 = randint(-10**30, 10**10)
        y2 = randint(-10**30, 10**10)

        C1 = C(x1, y1)
        C2 = C(x2, y2)
        assert (C1 == C2) == (C1.x == C2.x and C1.y == C2.y)
