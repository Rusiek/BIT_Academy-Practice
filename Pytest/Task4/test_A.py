from function import square
from random import randint
import pytest
class TestKlasa1:
    def test_1(self):
        for i in range(4):
            num=randint(-10,10)
            assert square(num)==num**2
class TestKlasa2:
    def test_2(self):
        for i in range(4):
            num=randint(-1000,1000)
            assert square(num)==num**2
class TestKlasa3:
    def test_3(self):
        for i in range(4):
            num=randint(-10000,1000000)
            assert square(num)==num**2
@pytest.mark.skipif(True, reason="problem")
class TestKlasa4:
    def test_4(self):
        for i in range(4):
            num=randint(-10**12,10**13)
            assert square(num)==num**2
# Napisać 4 klasy funkcji square
# Pierwsza zawiera kilka testów dla losowych liczb z przedziału <-10, 10>
# Druga zawiera kilka testów dla losowych liczb z przedziału <-1000, 1000>
# Trzecia zawiera kilka testów dla losowych liczb z przedziału <10 ** 4, 10 ** 6>
# Czwarta zawiera kilka testów dla losowych liczb z przedziału <10 ** 12, 10 ** 13>
# oraz marker skipif, który po wykonaniu uniemożliwi wykonanie testów z czwartej klasy
# ze względu na niepoprawne działanie funkcji w trzeciej klasie