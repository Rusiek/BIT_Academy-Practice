from function import is_prime

class TestMini:
    # Napisać testy sprawdzające funkcję is_prime dla liczb
    # z przedziału <-1, 6>
    def test_A(self):
        for i in range(-1, 7):
            if i < 2 or i == 4 or i == 6:
                assert is_prime(i) == False
            else:
                assert is_prime(i) == True

class TestMid:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # liczb z przedziału <10 ** 4, 10 ** 5>
    def test_A(self):
        tab = [60209, 23159, 99191]
        for i in tab:
            assert is_prime(i) == True
    def test_B(self):
        tab = [18357, 78891]
        for i in tab:
            assert is_prime(i) == False

class TestMaxi:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # z przedziału <10 ** 12, 10 ** 13>, a następnie
    # naprawić funkcję is_prime aby testy wykonywały się szybciej
    # niż dla aktualnej funkcji
    def test_A(self):
        tab = [2569800040597, 3769820150617]
        for i in tab:
            assert is_prime(i) == True
    def test_B(self):
        tab = [4761820120279, 1221829820379, 8241689830827]
        for i in tab:
            assert is_prime(i) == False
