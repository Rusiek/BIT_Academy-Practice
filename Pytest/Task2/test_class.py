from function import is_prime

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

# class TestMid:
#     # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
#     # liczb z przedziału <10 ** 4, 10 ** 5>

# class TestMaxi:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # z przedziału <10 ** 12, 10 ** 13>, a następnie
    # naprawić funkcję is_prime aby testy wykonywały się szybciej
    # niż dla aktualnej funkcji
