from function import square
# Napisać cztery testy z dla funckji square dla 0, 1, -1 i 100

def test_square_A():
    assert square(0) == 0
def test_square_B():
    assert square(1) == 1
def test_square_C():
    assert square(-1) == 1
def test_square_D():
    assert square(100) == 10000