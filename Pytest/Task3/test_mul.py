from cmplex import C

from random import randint

# Napisać testy sprawdzające mnożenie liczb zespolonych
# w załączonym pliku

class TestMini:

    def test1(self):
        assert C(0, 0) * C(0, 0) == C(0, 0)

    def test2(self):
        assert C(2, 1) * C(3, 7) == C(-1, 17)

    def test3(self):
        assert C(-3, -6) * C(-7, -9) == C(-33, 69)

    def test4(self):
        x1 = randint(-10**4, 10**4)
        x2 = randint(-10**4, 10**4)
        y1 = randint(-10**4, 10**4)
        y2 = randint(-10**4, 10**4)
        assert C(x1, y1) * C(x2, y2) == C(x1 * x2 - y1 * y2, x1 * y2 + y1 * x2)

class TestMaxi:

    def test1(self):
        x1 = randint(10**12, 10**13)
        x2 = randint(10**12, 10**13)
        y1 = randint(10**12, 10**13)
        y2 = randint(10**12, 10**13)
        assert C(x1, y1) * C(x2, y2) == C(x1 * x2 - y1 * y2, x1 * y2 + y1 * x2)

    def test2(self):
        x1 = randint(-10**13, -10**12)
        x2 = randint(-10**13, -10**12)
        y1 = randint(-10**13, -10**12)
        y2 = randint(-10**13, -10**12)
        assert C(x1, y1) * C(x2, y2) == C(x1 * x2 - y1 * y2, x1 * y2 + y1 * x2)

    def test3(self):
        x1 = randint(-10**13, -10**12)
        x2 = randint(10**12, 10**13)
        y1 = randint(-10**13, -10**12)
        y2 = randint(10**12, 10**13)
        assert C(x1, y1) * C(x2, y2) == C(x1 * x2 - y1 * y2, x1 * y2 + y1 * x2)

    def test4(self):
        x1 = randint(10**12, 10**13)
        x2 = randint(10**12, 10**13)
        y1 = randint(-10**13, -10**12)
        y2 = randint(-10**13, -10**12)
        assert C(x1, y1) * C(x2, y2) == C(x1 * x2 - y1 * y2, x1 * y2 + y1 * x2)