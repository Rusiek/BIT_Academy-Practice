from solution import is_prime
from is_prime_correct import is_prime2
from random import randint
import pytest

#dla warunków brzegowych
@pytest.mark.parametrize("test_input, expected", [(0, False), (1, False), (-1, False), (2, True), (3, True)])

def boundary_conditions(test_input, expected):
    assert is_prime(test_input) == expected



class Min:
    def test_mid1(self):
        assert is_prime(-100) == is_prime2(-100)
    def test_mid2(self):
        assert is_prime(100) == is_prime2(100)
    def test_mid3(self):
        num = randint(10, 1000)
        assert is_prime(num) == is_prime2(num)
    def test_mid4(self):
        num = randint(10, 1000)
        assert is_prime(num) == is_prime2(num)
    def test_mid5(self):
        num = randint(10, 10000)
        assert is_prime(num) == is_prime2(num)


class Mid:
    def test_mid1(self):
        assert is_prime(10**4) == is_prime2(10**4)
    def test_mid2(self):
        assert is_prime(10**5) == is_prime2(10**5)
    def test_mid3(self):
        num = randint(10**4, 10**5)
        assert is_prime(num) == is_prime2(num)
    def test_mid4(self):
        num = randint(10**4, 10**5)
        assert is_prime(num) == is_prime2(num)
    def test_mid5(self):
        num = randint(10**4, 10**5)
        assert is_prime(num) == is_prime2(num)


class Maxi:
    def test_maxi1(self):
        assert is_prime(10**12) == is_prime2(10**12)
    def test_maxi2(self):
        assert is_prime(10**13) == is_prime2(10**13)
    def test_maxi3(self):
        num = randint(10**12, 10**13)
        assert is_prime(num) == is_prime2(num)
    def test_maxi4(self):
        num = randint(10**12, 10**13)
        assert is_prime(num) == is_prime2(num)
    def test_maxi5(self):
        num = randint(10**12, 10**13)
        assert is_prime(num) == is_prime2(num)