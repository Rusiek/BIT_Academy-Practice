import py
from function import square
from random import randint
import pytest

# Napisać 4 klasy funkcji square
# Pierwsza zawiera kilka testów dla losowych liczb z przedziału <-10, 10>
class TestMini:

    def test1(self):
        x = randint(-10, 10)
        assert x ** 2 == square(x)
    
    def test2(self):
        x = randint(-10, 10)
        assert x ** 2 == square(x)
    
    def test3(self):
        x = randint(-10, 10)
        assert x ** 2 == square(x)
    
    def test4(self):
        x = randint(-10, 10)
        assert x ** 2 == square(x)


# Druga zawiera kilka testów dla losowych liczb z przedziału <-1000, 1000>
class TestMidi:

    def test1(self):
        x = randint(-1000, 1000)
        assert x ** 2 == square(x)
    
    def test2(self):
        x = randint(-1000, 1000)
        assert x ** 2 == square(x)
    
    def test3(self):
        x = randint(-1000, 1000)
        assert x ** 2 == square(x)
    
    def test4(self):
        x = randint(-1000, 1000)
        assert x ** 2 == square(x)


# Trzecia zawiera kilka testów dla losowych liczb z przedziału <10 ** 4, 10 ** 6>
class TestMaxi:

    def test1(self):
        x = randint(10 ** 4, 10 ** 6)
        assert x ** 2 == square(x)
    
    def test2(self):
        x = randint(10 ** 4, 10 ** 6)
        assert x ** 2 == square(x)
    
    def test3(self):
        x = randint(10 ** 4, 10 ** 6)
        assert x ** 2 == square(x)
    
    def test4(self):
        x = randint(10 ** 4, 10 ** 6)
        assert x ** 2 == square(x)


# Czwarta zawiera kilka testów dla losowych liczb z przedziału <10 ** 12, 10 ** 13>
# oraz marker skipif, który po wykonaniu uniemożliwi wykonanie testów z czwartej klasy
# ze względu na niepoprawne działanie funkcji w trzeciej klasie

@pytest.mark.skipif(TestMaxi == pytest.fail)        #?
class TestHuge:
    
    def test1(self):
        x = randint(10 ** 12, 10 ** 13)
        assert x ** 2 == square(x)
    
    def test2(self):
        x = randint(10 ** 12, 10 ** 13)
        assert x ** 2 == square(x)
    
    def test3(self):
        x = randint(10 ** 12, 10 ** 13)
        assert x ** 2 == square(x)
    
    def test4(self):
        x = randint(10 ** 12, 10 ** 13)
        assert x ** 2 == square(x)