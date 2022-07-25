import pytest
from function import is_prime
from function import next_primary
from random import randint

def correct_function(n):
    n += 1
    while is_prime(n) == False:
        n += 1
    return n


class BoundaryConditions:

    @pytest.mark.parametrize("number, expected", [(-1, 2), (0, 2), (1, 2), (2, 3), (3, 5), (4, 5)])

    def test(number, expected):
        assert next_primary(number) == expected


class TestMini:

    @pytest.mark.parametrize("number", [randint(4, 100) for _ in range (5)])

    def test_mini(self, number):
        assert next_primary(number) == correct_function(number)


class TestMid:

    @pytest.mark.parametrize("number", [randint(4, 10*5) for _ in range (5)])

    def test_mid(self, number):
        assert next_primary(number) == correct_function(number)


class TestMaxi:

    @pytest.mark.parametrize("number", [randint(4, 10*14) for _ in range (5)])

    def test_maxi(self, number):
        assert next_primary(number) == correct_function(number)



class TestBoss:

    @pytest.mark.parametrize("number", [randint(10**10, 10**16) for _ in range (5)])

    def test_boss(self, number):
        assert next_primary(number) == correct_function(number)

    
