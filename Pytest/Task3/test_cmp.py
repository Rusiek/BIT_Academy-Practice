from cmplex import C

from random import randint

# Napisać testy sprawdzające porównywanie liczb zespolonych
# w załączonym pliku

class TestMini:

    def test1(self):
        assert C(0, 0) == C(0, 0)

    def test2(self):
        assert C(2137, 9001) == C(2137, 9001)
    
    def test3(self):
        x = randint(10, 10**4)
        y = randint(10, 10**4)
        assert C(x, y) == C(x, y)

    def test4(self):
        x = -1 * randint(10, 10**4)
        y =  -1 * randint(10, 10**4)
        assert C(x, y) == C(x, y)

class TestMaxi:
    
    def test1(self):
        x = randint(10**12, 10**13)
        y = randint(10**12, 10**13)
        assert C(x, y) == C(x, y)

    def test2(self):
        x = -1 * randint(10**12, 10**13)
        y =  -1 * randint(10**12, 10**13)
        assert C(x, y) == C(x, y)

    def test3(self):
        x = -1 * randint(10**12, 10**13)
        y =  randint(10**12, 10**13)
        assert C(x, y) == C(x, y)

    def test4(self):
        x =  randint(10**12, 10**13)
        y =  -1 * randint(10**12, 10**13)
        assert C(x, y) == C(x, y)