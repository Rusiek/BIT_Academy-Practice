from function import is_prime

class TestMini:
    def test_1(self):
        assert is_prime(-1)==False
    def test_2(self):
        assert is_prime(0)==False
    def test_3(self):
        assert is_prime(1)==False
    def test_4(self):
        assert is_prime(2)==True
    def test_5(self):
        assert is_prime(3)==True
    def test_6(self):
        assert is_prime(4)==False
    def test_7(self):
        assert is_prime(5)==True
    def test_71(self):
        assert is_prime(6)==False
    # Napisać testy sprawdzające funkcję is_prime dla liczb
    # z przedziału <-1, 6>

class TestMid:
    def test_8(self):
        assert is_prime(56743)==False
    def test_9(self):
        assert is_prime(393919)==True
    def test_10(self):
        assert is_prime(423302)==False
    def test_11(self):
        assert is_prime(19937)==True
    def test_12(self):
        assert is_prime(23442)==False
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # liczb z przedziału <10 ** 4, 10 ** 5>

class TestMaxi:
    def test_13(self):
        assert is_prime(1000123465987)==True
    def test_14(self):
        assert is_prime(1012345678901)==True
    def test_15(self):
        assert is_prime(100000000000)==False
    def test_16(self):
        assert is_prime(1043677052928)==False
    def test_17(self):
        assert is_prime(28611311719724)==False
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # z przedziału <10 ** 12, 10 ** 13>, a następnie
    # naprawić funkcję is_prime aby testy wykonywały się szybciej
    # niż dla aktualnej funkcji
