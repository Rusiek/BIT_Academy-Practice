import pytest
from solution import is_prime

class TestMini:
    test_array = [(-1, False), (0, False), (1, False), (2, True), (3, True), (4, False), (5, True), (6, False), (7, True)]
    @pytest.mark.parametrize("test_input, expected", test_array)
    def test(self, test_input, expected):
        assert is_prime(test_input) == expected

class TestMid:
    def test_A(self):
        tab = [60209, 23159, 99191]
        for i in tab:
            assert is_prime(i) == True
    def test_B(self):
        tab = [18357, 78891, 99838, 67222]
        for i in tab:
            assert is_prime(i) == False

class TestMaxi:
    def test_A(self):
        tab = [2569800040597, 3769820150617]
        for i in tab:
            assert is_prime(i) == True
    def test_B(self):
        tab = [4761820120279, 1221829820379, 8241689830827]
        for i in tab:
            assert is_prime(i) == False
