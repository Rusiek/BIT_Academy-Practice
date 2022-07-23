# test_sol.py - plik ma zawierać testy do funkcji zawartej w solution.py, zastanowić się
#               nad sposobem generowania testów oraz sposobu grupowania ich w klasy.

import pytest

from solution import is_prime

from is_prime import is_prime_correct

from random import randint

special_test = [(0, False), (1, False), (2, True), (3, True), (-1, False)]

@pytest.mark.parametrize("test_input, expected", special_test)
def test_special(test_input, expected):
    assert is_prime(test_input) == expected

class TestMini:

    def test1(self):
        x = randint(-10, -1)
        assert is_prime_correct(x) == is_prime(x)
    
    def test2(self):
        x = randint(-100, -10)
        assert is_prime_correct(x) == is_prime(x)

    def test3(self):
        x = randint(4, 20)
        assert is_prime_correct(x) == is_prime(x)

    def test4(self):
        x = randint(4, 100)
        assert is_prime_correct(x) == is_prime(x)

    def test5(self):
        x = randint(100, 1000)
        assert is_prime_correct(x) == is_prime(x)
    
  
class TestMid:

    def test1(self):
        x = randint(10 ** 4, 10 ** 5)
        assert is_prime_correct(x) == is_prime(x)
    
    def test2(self):
        x = randint(10 ** 4, 10 ** 5)
        assert is_prime_correct(x) == is_prime(x)
    
    def test3(self):
        x = randint(10 ** 4, 10 ** 5)
        assert is_prime_correct(x) == is_prime(x)
    
    def test4(self):
        x = randint(10 ** 4, 10 ** 5)
        assert is_prime_correct(x) == is_prime(x)
    
    def test5(self):
        x = randint(-10 ** 5, -10 ** 4)
        assert is_prime_correct(x) == is_prime(x)


class TestMaxi:

    def test1(self):
        x = randint(10 ** 12, 10 ** 13)
        assert is_prime_correct(x) == is_prime(x)
    
    def test2(self):
        x = randint(10 ** 12, 10 ** 13)
        assert is_prime_correct(x) == is_prime(x)
    
    def test3(self):
        x = randint(10 ** 12, 10 ** 13)
        assert is_prime_correct(x) == is_prime(x)
    
    def test4(self):
        x = randint(10 ** 12, 10 ** 13)
        assert is_prime_correct(x) == is_prime(x)
    
    def test5(self):
        x = randint(-10 ** 13, -10 ** 12)
        assert is_prime_correct(x) == is_prime(x)

