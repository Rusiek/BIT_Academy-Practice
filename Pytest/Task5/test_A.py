import pytest
from function import count_chars

# Napisać testy dla funkcji count_chars za pomocą
# markera "parametrize"

# Funkcja count_chars zwraca trzyelementową tablicę
# która zawiera odpowiednio liczbę wystąpień znaku 'a', 'b' i 'c'

@pytest.mark.parametrize("input, expected", [("aaa", [3, 0, 0]), ("aba", [2, 1, 0]), ("cab", [1, 1, 1])])
def test(input, expected):
    assert count_chars(input) == expected