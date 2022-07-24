import pytest
from function import count_chars

# Napisać testy dla funkcji count_chars za pomocą
# markera "parametrize"

# Funkcja count_chars zwraca trzyelementową tablicę
# która zawiera odpowiednio liczbę wystąpień znaku 'a', 'b' i 'c'


@pytest.mark.parametrize("test_input, expected", [("aaa", [3, 0, 0]), ("bbb", [0, 3, 0]), ("ccc", [0, 0, 3]), ("abc", [1, 1, 1]), ("aabbccababcabcb", [5, 6, 4])] )

def test(test_input, expected):
    assert count_chars(test_input) == expected
