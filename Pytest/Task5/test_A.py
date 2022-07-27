import pytest
from function import count_chars

# Napisać testy dla funkcji count_chars za pomocą
# markera "parametrize"

# Funkcja count_chars zwraca trzyelementową tablicę
# która zawiera odpowiednio liczbę wystąpień znaku 'a', 'b' i 'c'


class Test1:
    A = [('aabbc', [2, 2, 1]),
         ('abac', [2, 1, 1]),
         (('bbbbb'), [0, 5, 0]),
         (('abcba', [2, 2, 1]))]

    @pytest.mark.parametrize('s,sol', A)
    def test_A(self, s, sol):
        assert count_chars(s) == sol
