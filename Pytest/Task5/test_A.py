import pytest
from function import count_chars

@pytest.mark.parametrize("num, output",[("aabbcc",[2,2,2]),("aaabbcccccc",[3,2,6]),("aaabbbbbc",[3,5,1]),("aaaacc",[4,0,2])])
def test_multiplication_11(num, output):
   assert count_chars(num) == output

# Napisać testy dla funkcji count_chars za pomocą
# markera "parametrize"

# Funkcja count_chars zwraca trzyelementową tablicę
# która zawiera odpowiednio liczbę wystąpień znaku 'a', 'b' i 'c'