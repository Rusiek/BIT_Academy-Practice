from random import randint
import pytest
from function import fast_prime
from function import ex

def find(n):
    n += 1
    while not fast_prime(n):
        n += 1
    return n

class TestEdge:
    @pytest.mark.parametrize("x", [-1, 0, 1, 2, 3])
    def test(self, x):
        assert find(x) == ex(x)

class TestMin:
    @pytest.mark.parametrize("x", [randint(0, 100) for _ in range(20)])
    def test(self, x):
        assert find(x) == ex(x)
        
class TestMid:
    @pytest.mark.parametrize("x", [randint(10 ** 3, 10 ** 6) for _ in range(20)])
    def test(self, x):
        assert find(x) == ex(x)
        
class TestMax:
    @pytest.mark.parametrize("x", [randint(10 ** 10, 10 ** 14) for _ in range(20)])
    def test(self, x):
        assert find(x) == ex(x)
    
