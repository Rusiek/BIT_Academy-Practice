# Drugi zawiera testy sprawdzającymi czy rzeczywiście podana liczba jest najmniejszą liczbą większą od "n",
# zastanowić się nad sposobem generowania testów oraz sposobu grupowania ich w klasy

import pytest
from function import function, is_prime
from random import randint


def find_next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n


class TestSpecial:
    tests = [-1, 0, 1, 2, 3]

    @pytest.mark.parametrize("n", tests)
    def test(self, n):
        assert function(n) == find_next_prime(n)


class TestMini:
    tests = [randint(-10, 100) for _ in range(5)]

    @pytest.mark.parametrize("n", tests)
    def test(self, n):
        assert function(n) == find_next_prime(n)


class TestMidi:
    tests = [randint(100, 10**4) for _ in range(5)]

    @pytest.mark.parametrize("n", tests)
    def test(self, n):
        assert function(n) == find_next_prime(n)


class TestMaxi:
    tests = [randint(10**5, 10**9) for _ in range(5)]

    @pytest.mark.parametrize("n", tests)
    def test(self, n):
        assert function(n) == find_next_prime(n)


class TestHudge:
    tests = [randint(10**10, 10**14) for _ in range(5)]

    @pytest.mark.parametrize("n", tests)
    def test(self, n):
        assert function(n) == find_next_prime(n)