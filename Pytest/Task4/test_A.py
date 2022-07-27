from function import square
from random import randint
import pytest

# Napisać 4 klasy funkcji square
# Pierwsza zawiera kilka testów dla losowych liczb z przedziału <-10, 10>
# Druga zawiera kilka testów dla losowych liczb z przedziału <-1000, 1000>
# Trzecia zawiera kilka testów dla losowych liczb z przedziału <10 ** 4, 10 ** 6>
# Czwarta zawiera kilka testów dla losowych liczb z przedziału <10 ** 12, 10 ** 13>
# oraz marker skipif, który po wykonaniu uniemożliwi wykonanie testów z czwartej klasy
# ze względu na niepoprawne działanie funkcji w trzeciej klasie


class Test1:
    def test_A(self):
        x = randint(-10, 10)
        assert square(x) == x**2

    def test_B(self):
        x = randint(-10, 10)
        assert square(x) == x**2

    def test_C(self):
        x = randint(-10, 10)
        assert square(x) == x**2

    def test_D(self):
        x = randint(-10, 10)
        assert square(x) == x**2

    def test_E(self):
        x = randint(-10, 10)
        assert square(x) == x**2


class Test2:
    def test_A(self):
        x = randint(-1000, 1000)
        assert square(x) == x**2

    def test_B(self):
        x = randint(-1000, 1000)
        assert square(x) == x**2

    def test_C(self):
        x = randint(-1000, 1000)
        assert square(x) == x**2

    def test_D(self):
        x = randint(-1000, 1000)
        assert square(x) == x**2

    def test_E(self):
        x = randint(-1000, 1000)
        assert square(x) == x**2


class Test3:
    def test_A(self):
        x = randint(10**4, 10**6)
        assert square(x) == x**2

    def test_B(self):
        x = randint(10**4, 10**6)
        assert square(x) == x**2

    def test_C(self):
        x = randint(10**4, 10**6)
        assert square(x) == x**2

    def test_D(self):
        x = randint(10**4, 10**6)
        assert square(x) == x**2

    def test_E(self):
        x = randint(10**4, 10**6)
        assert square(x) == x**2


@pytest.mark.skipif
class Test4:
    def test_A(self):
        x = randint(10**12, 10**13)
        assert square(x) == x**2

    def test_B(self):
        x = randint(10**12, 10**13)
        assert square(x) == x**2

    def test_C(self):
        x = randint(10**12, 10**13)
        assert square(x) == x**2

    def test_D(self):
        x = randint(10**12, 10**13)
        assert square(x) == x**2

    def test_E(self):
        x = randint(10**12, 10**13)
        assert square(x) == x**2