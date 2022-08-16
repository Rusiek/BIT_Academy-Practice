from random import randint
from function import square
import pytest

# Napisać 4 klasy funkcji square
# Pierwsza zawiera kilka testów dla losowych liczb z przedziału <-10, 10>
# Druga zawiera kilka testów dla losowych liczb z przedziału <-1000, 1000>
# Trzecia zawiera kilka testów dla losowych liczb z przedziału <10 ** 4, 10 ** 6>
# Czwarta zawiera kilka testów dla losowych liczb z przedziału <10 ** 12, 10 ** 13>
# oraz marker skipif, który po wykonaniu uniemożliwi wykonanie testów z czwartej klasy
# ze względu na niepoprawne działanie funkcji w trzeciej klasie
class TestMini:
    def test_A(self):
        assert square(0) == 0

    def test_B(self):
        assert square(1) == 1

    def test_C(self):
        assert square(-1) == 1

    def test_D(self):
        assert square(5) == 25

class TestMid:
    def test_A(self):
        assert square(-1000) == 1000000

    def test_B(self):
        assert square(1000) == 1000000
    
    def test_C(self):
        for i in range(5):
            number = randint(-1000, 1000)
            assert square(number) == number * number

class TestBig:
    def test_A(self):
        assert square(10 ** 4) == 10 ** 8
    
    def test_B(self):
        assert square(10 ** 6) == 10 ** 12
    
    def test_C(self):
        for i in range(5):
            number = randint(10 ** 4, 10 ** 6)
            assert square(number) == number * number

@pytest.mark.skipif(TestBig, reason="TestBig doesn't work")
class TestHuge:
    def test_A(self):
        assert square(10 ** 12) == 10 ** 24
    
    def test_B(self):
        assert square(10 ** 13) == 10 ** 26
    
    def test_C(self):
        for i in range(5):
            number = randint(10 ** 12, 10 ** 13)
            assert square(number) == number * number