
# from Pytest.Task6.solution import isPrime
from solution import fast_prime
from random import randint
import pytest

def isPrime(n):
      
    # Corner case
    if n <= 1:
        return False
  
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False;
  
    return True

class TestCorner:
    @pytest.mark.parametrize("x", [0, 1, 2, 3, 5, 7])
    def test(self, x):
        assert fast_prime(x) == isPrime(x)

class TestMid:
    @pytest.mark.parametrize("x", [randint(10*5, 10 *7) for _ in range(100)])
    def test(self, x):
        assert fast_prime(x) == isPrime(x)


class TestMaxi:

    @pytest.mark.parametrize("x", [randint(10*20, 10 *30) for _ in range(100)])
    def test(self, x):
        assert fast_prime(x) == isPrime(x)