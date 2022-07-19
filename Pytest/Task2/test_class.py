from function import is_prime
from function2 import is_prime2
from random import randint

class TestMini:
    # Napisać testy sprawdzające funkcję is_prime dla liczb
    # z przedziału <-1, 6>
    def test_0(self):
        x = -1
        assert is_prime(x) == is_prime2(x)

    def test_1(self):
        x = 0
        assert is_prime(x) == is_prime2(x)
    
    def test_2(self):
        x = 1
        assert is_prime(x) == is_prime2(x)

    def test_3(self):
        x = 2
        assert is_prime(x) == is_prime2(x)
    
    def test_4(self):
        x = 3
        assert is_prime(x) == is_prime2(x)
    
    def test_5(self):
        x = 4
        assert is_prime(x) == is_prime2(x)

    def test_6(self):
        x = 5
        assert is_prime(x) == is_prime2(x)

    def test_7(self):
        x = 6
        assert is_prime(x) == is_prime2(x)
    
    

class TestMid:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # liczb z przedziału <10 ** 4, 10 ** 5>
    def test_0(self):
        x = randint(10 ** 4, 10 **5)
        assert is_prime(x) == is_prime2(x)

    def test_1(self):
        x = randint(10 ** 4, 10 **5)
        assert is_prime(x) == is_prime2(x)
    
    def test_2(self):
        x = randint(10 ** 4, 10 **5)
        assert is_prime(x) == is_prime2(x)
    
    def test_3(self):
        x = randint(10 ** 4, 10 **5)
        assert is_prime(x) == is_prime2(x)

    def test_4(self):
        x = randint(10 ** 4, 10 **5)
        assert is_prime(x) == is_prime2(x)

class TestMaxi:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # z przedziału <10 ** 12, 10 ** 13>, a następnie
    # naprawić funkcję is_prime aby testy wykonywały się szybciej
    # niż dla aktualnej funkcji
    def test_0(self):
        x = randint(10 ** 12, 10 ** 13)
        assert is_prime(x) == is_prime2(x)

    def test_1(self):
        x = randint(10 ** 12, 10 ** 13)
        assert is_prime(x) == is_prime2(x)
    
    def test_2(self):
        x = randint(10 ** 12, 10 ** 13)
        assert is_prime(x) == is_prime2(x)
    
    def test_3(self):
        x = randint(10 ** 12, 10 ** 13)
        assert is_prime(x) == is_prime2(x)

    def test_4(self):
        x = randint(10 ** 12, 10 ** 13)
        assert is_prime(x) == is_prime2(x)
