from random import randint

from function import is_prime

from function2 import is_prime_correct


class TestMini:
    # Napisać testy sprawdzające funkcję is_prime dla liczb
    # z przedziału <-1, 6>
    def test(self):
        for x in range(-1, 7):
            assert is_prime_correct(x) == is_prime(x)


class TestMid:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # liczb z przedziału <10 ** 4, 10 ** 5>
    def test(self):
        for _ in range(5):
            x = randint(10 ** 4, 10 ** 5)
            assert is_prime_correct(x) == is_prime(x)
    

class TestMaxi:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # z przedziału <10 ** 12, 10 ** 13>, a następnie
    # naprawić funkcję is_prime aby testy wykonywały się szybciej
    # niż dla aktualnej funkcji
    def test(self):
        for _ in range(5):
            x = randint(10 ** 12, 10 ** 13)
            assert is_prime_correct(x) == is_prime(x)
        
    