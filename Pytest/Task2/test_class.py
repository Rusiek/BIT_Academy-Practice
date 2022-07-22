from random import randint

from function import is_prime

from function2 import is_prime_correct


class TestMini:
    # Napisać testy sprawdzające funkcję is_prime dla liczb
    # z przedziału <-1, 6>
    def test1(self):
        x = -1 
        assert is_prime_correct(x) == is_prime(x)
    
    def test1(self):
        x = 0 
        assert is_prime_correct(x) == is_prime(x)
    
    def test2(self):
        x = 1 
        assert is_prime_correct(x) == is_prime(x)

    def test3(self):
        x = 2 
        assert is_prime_correct(x) == is_prime(x)

    def test4(self):
        x = 3 
        assert is_prime_correct(x) == is_prime(x)

    def test5(self):
        x = 4 
        assert is_prime_correct(x) == is_prime(x)
    
    def test6(self):
        x = 5 
        assert is_prime_correct(x) == is_prime(x)
    
    def test7(self):
        x = 6
        assert is_prime_correct(x) == is_prime(x)


class TestMid:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # liczb z przedziału <10 ** 4, 10 ** 5>
    def test1(self):
        x = randint(10 ** 4, 10 ** 5)
        assert is_prime_correct(x) == is_prime(x)
    
    def test2(self):
        x = randint(10 ** 4, 10 ** 5)
        assert is_prime_correct(x) == is_prime(x)
    
    def test3(self):
        x = randint(10 ** 4, 10 ** 5)
        assert is_prime_correct(x) == is_prime(x)
    
    def test4(self):
        x = randint(10 ** 4, 10 ** 5)
        assert is_prime_correct(x) == is_prime(x)
    
    def test5(self):
        x = randint(10 ** 4, 10 ** 5)
        assert is_prime_correct(x) == is_prime(x)


class TestMaxi:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # z przedziału <10 ** 12, 10 ** 13>, a następnie
    # naprawić funkcję is_prime aby testy wykonywały się szybciej
    # niż dla aktualnej funkcji

    def test1(self):
        x = randint(10 ** 12, 10 ** 13)
        assert is_prime_correct(x) == is_prime(x)
    
    def test2(self):
        x = randint(10 ** 12, 10 ** 13)
        assert is_prime_correct(x) == is_prime(x)
    
    def test3(self):
        x = randint(10 ** 12, 10 ** 13)
        assert is_prime_correct(x) == is_prime(x)
    
    def test4(self):
        x = randint(10 ** 12, 10 ** 13)
        assert is_prime_correct(x) == is_prime(x)
    
    def test5(self):
        x = randint(10 ** 12, 10 ** 13)
        assert is_prime_correct(x) == is_prime(x)

