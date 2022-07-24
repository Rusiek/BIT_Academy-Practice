from function import is_prime
from fast_alg import fast_prime
from random import randint
class TestMini:
    # Napisać testy sprawdzające funkcję is_prime dla liczb
    # z przedziału <-1, 6>
    def test_one(self):
        assert is_prime(-1) == True
    def test_two(self):
        assert is_prime(0) == False
    def test_three(self):
        assert is_prime(1) == False
    def test_four(self):
        assert is_prime(2) == True
    def test_five(self):
        assert is_prime(3) == True
    def test_six(self):
        assert is_prime(4) == False
    def test_seven(self):
        assert is_prime(5) == True
    def test_eight(self):
        assert is_prime(6) == False

class TestMid:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # liczb z przedziału <10 ** 4, 10 ** 5>
    def test_one(self):
        i = randint(10 ** 4, 10 ** 5)
        assert is_prime(i) == fast_prime(i)
    def test_two(self):
        i = randint(10 ** 4, 10 ** 5)
        assert is_prime(i) == fast_prime(i)
    def test_three(self):
        i = randint(10 ** 4, 10 ** 5)
        assert is_prime(i) == fast_prime(i)
    def test_four(self):
        i = randint(10 ** 4, 10 ** 5)
        assert is_prime(i) == fast_prime(i)
    def test_five(self):
        i = randint(10 ** 4, 10 ** 5)
        assert is_prime(i) == fast_prime(i)
    

class TestMaxi:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # z przedziału <10 ** 12, 10 ** 13>, a następnie
    # naprawić funkcję is_prime aby testy wykonywały się szybciej
    # niż dla aktualnej funkcji
    def test_one(self):
        i = randint(10 ** 12, 10 ** 13)
        assert is_prime(i) == fast_prime(i)
    def test_two(self):
        i = randint(10 ** 12, 10 ** 13)
        assert is_prime(i) == fast_prime(i)
    def test_three(self):
        i = randint(10 ** 12, 10 ** 13)
        assert is_prime(i) == fast_prime(i)
    def test_four(self):
        i = randint(10 ** 12, 10 ** 13)
        assert is_prime(i) == fast_prime(i)
    def test_five(self):
        i = randint(10 ** 12, 10 ** 13)
        print(i)
        assert is_prime(i) == fast_prime(i)    

