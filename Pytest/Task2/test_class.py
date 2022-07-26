from function import is_prime
from random import randint
from sol import sol


class TestMini:
    # Napisać testy sprawdzające funkcję is_prime dla liczb
    # z przedziału <-1, 6>
    def test_A(self):
        x = randint(-1, 6)
        assert is_prime(x) == sol(x)

    def test_B(self):
        x = randint(-1, 6)
        assert is_prime(x) == sol(x)


class TestMid:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # liczb z przedziału <10 ** 4, 10 ** 5>
    def test_A(self):
        x = randint(10**4, 10**5)
        assert is_prime(x) == sol(x)

    def test_B(self):
        x = randint(10**4, 10**5)
        assert is_prime(x) == sol(x)

    def test_C(self):
        x = randint(10**4, 10**5)
        assert is_prime(x) == sol(x)

    def test_D(self):
        x = randint(10**4, 10**5)
        assert is_prime(x) == sol(x)

    def test_E(self):
        x = randint(10**4, 10**5)
        assert is_prime(x) == sol(x)


class TestMaxi:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # z przedziału <10 ** 12, 10 ** 13>, a następnie
    # naprawić funkcję is_prime aby testy wykonywały się szybciej
    # niż dla aktualnej funkcji
    def test_A(self):
        x = randint(10**12, 10**13)
        assert is_prime(x) == sol(x)

    def test_B(self):
        x = randint(10**12, 10**13)
        assert is_prime(x) == sol(x)

    def test_C(self):
        x = randint(10**12, 10**13)
        assert is_prime(x) == sol(x)

    def test_D(self):
        x = randint(10**12, 10**13)
        assert is_prime(x) == sol(x)

    def test_E(self):
        x = randint(10**12, 10**13)
        assert is_prime(x) == sol(x)
