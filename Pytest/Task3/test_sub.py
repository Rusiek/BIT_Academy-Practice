from cmplex import C
from random import randint
# Napisać testy sprawdzające odejmowanie liczb zespolonych
# w załączonym pliku


class TestSub:
    def test_A(self):
        x1 = randint(0, 10**10)
        x2 = randint(0, 10**10)

        y1 = randint(0, 10**10)
        y2 = randint(0, 10**10)

        res = C(x1, y1) - C(x2, y2)
        assert res.x == x1 - x2 and res.y == y1 - y2

    def test_B(self):
        x1 = randint(10**10, 10**20)
        x2 = randint(10**10, 10**20)

        y1 = randint(10**10, 10**20)
        y2 = randint(10**10, 10**20)

        res = C(x1, y1) - C(x2, y2)
        assert res.x == x1 - x2 and res.y == y1 - y2

    def test_C(self):
        x1 = randint(-10**30, 10**10)
        x2 = randint(-10**30, 10**10)

        y1 = randint(-10**30, 10**10)
        y2 = randint(-10**30, 10**10)

        res = C(x1, y1) - C(x2, y2)
        assert res.x == x1 - x2 and res.y == y1 - y2
