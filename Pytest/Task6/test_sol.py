from solution import is_prime
import pytest
class TestOne:
    @pytest.mark.parametrize("num, output",[(-1,False),(0,False),(2,True),(5,True),])
    def test_male(self, num, output):
        assert is_prime(num)==output
class TestTwo:
    @pytest.mark.parametrize("num, output",[(56743,False),(423302,False),(19937,True)])
    def test_middle(self, num, output):
        assert is_prime(num)==output
class TestThree:
    @pytest.mark.parametrize("num, output",[(100000000000,False),(1043677052928,False),(1000123465987,True)])
    def test_big(self, num, output):
        assert is_prime(num)==output