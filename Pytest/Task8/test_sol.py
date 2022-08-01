from sol import fun
import pytest
class TestOne:
    @pytest.mark.parametrize("num, output",[(-1,2),(0,2),(2,2),(5,5),])
    def test_male(self, num, output):
        assert fun(num)==output
class TestTwo:
    @pytest.mark.parametrize("num, output",[(56743,56747),(423302,423307),(19937,19937)])
    def test_middle(self, num, output):
        assert fun(num)==output
class TestThree:
    @pytest.mark.parametrize("num, output",[(100000000000,100000000003),(1043677052928,1043677052941),(1000123465987,1000123465987)])
    def test_big(self, num, output):
        assert fun(num)==output


