from function import is_prime

class TestMini:
    # Napisać testy sprawdzające funkcję is_prime dla liczb
    # z przedziału <-1, 6>
    def test_A(self):
        assert is_prime(-1) == False
        assert is_prime(0) == False
        assert is_prime(1) == False
        assert is_prime(2) == True
        assert is_prime(3) == True
        assert is_prime(6) == False

class TestMid:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # liczb z przedziału <10 ** 4, 10 ** 5>
    def test_A(self):
        assert is_prime(10000) == False
        assert is_prime(18901) == False
        assert is_prime(44129) == True
        assert is_prime(64663) == True
        assert is_prime(81011) == False

class TestMaxi:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # z przedziału <10 ** 12, 10 ** 13>, a następnie
    # naprawić funkcję is_prime aby testy wykonywały się szybciej
    # niż dla aktualnej funkcji
    def test_A(self):
        assert is_prime(123973328923) == True
        assert is_prime(352656328916) == False
        assert is_prime(552656290929) == False
        assert is_prime(915989937499) == False
        assert is_prime(995779999767) == False
