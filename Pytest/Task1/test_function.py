from function import square
# Napisać cztery testy z dla funckji square dla 0, 1, -1 i 100

def test_square():
    assert square(0) == 0
    assert square(1) == 1
    assert square(-1) == 1
    assert square(100) == 10000

test_square()