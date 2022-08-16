import pytest
from function import count_chars

# Napisać testy dla funkcji count_chars za pomocą
# markera "parametrize"

# Funkcja count_chars zwraca trzyelementową tablicę
# która zawiera odpowiednio liczbę wystąpień znaku 'a', 'b' i 'c'

test_array = [("", [0, 0, 0]), ("abc", [1, 1, 1]), ("aaa", [3, 0, 0]), ("accacccccac", [3, 0, 8]), ("abccbabbbcaaccab", [5, 6, 5])]

@pytest.mark.parametrize("test_input, expected", test_array)
def test(test_input, expected):
    assert count_chars(test_input) == expected